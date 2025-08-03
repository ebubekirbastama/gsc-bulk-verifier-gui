import tkinter as tk
from tkinter import filedialog, messagebox
from google.oauth2 import service_account
from googleapiclient.discovery import build
import threading

class GSCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 GSC Toplu Domain Ekleme & Doğrulama Aracı")
        self.root.geometry("600x300")

        self.domain_file = None
        self.api_key_file = None
        self.domains = []

        # Arayüz
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self.root, text="📂 Domain Listesi Yükle (.txt)", command=self.load_domain_file).pack(pady=10)
        tk.Button(self.root, text="🔐 API JSON Dosyasını Seç", command=self.load_api_key_file).pack(pady=10)
        tk.Button(self.root, text="🚀 GSC Ekle ve Doğrula", bg="green", fg="white", command=self.run_in_thread).pack(pady=15)

        self.log = tk.Text(self.root, height=10, width=80)
        self.log.pack()

    def load_domain_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                self.domains = [line.strip() for line in f if line.strip()]
            self.log.insert(tk.END, f"[+] {len(self.domains)} domain yüklendi.\n")

    def load_api_key_file(self):
        self.api_key_file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if self.api_key_file:
            self.log.insert(tk.END, "[+] API anahtar dosyası yüklendi.\n")

    def run_in_thread(self):
        threading.Thread(target=self.process_domains).start()

    def process_domains(self):
        if not self.domains or not self.api_key_file:
            messagebox.showerror("Eksik Bilgi", "Lütfen önce domain listesi ve API anahtar dosyasını seçin.")
            return

        try:
            creds = service_account.Credentials.from_service_account_file(
                self.api_key_file,
                scopes=['https://www.googleapis.com/auth/webmasters', 'https://www.googleapis.com/auth/siteverification']
            )
            webmasters = build('webmasters', 'v3', credentials=creds)
            verifier = build('siteVerification', 'v1', credentials=creds)
        except Exception as e:
            self.log.insert(tk.END, f"[!] API bağlantısı kurulamadı: {e}\n")
            return

        for domain in self.domains:
            site_url = domain if domain.startswith("http") else f"http://{domain}/"

            try:
                webmasters.sites().add(siteUrl=site_url).execute()
                self.log.insert(tk.END, f"[✓] {site_url} GSC'ye eklendi.\n")
            except Exception as e:
                self.log.insert(tk.END, f"[!] {site_url} eklenemedi: {e}\n")

            try:
                verification_body = {
                    "verificationMethod": "FILE",
                    "site": {
                        "type": "SITE",
                        "identifier": site_url
                    }
                }
                verifier.webResource().insert(verificationMethod="FILE", body=verification_body).execute()
                self.log.insert(tk.END, f"[✓] {site_url} doğrulandı.\n")
            except Exception as e:
                self.log.insert(tk.END, f"[!] {site_url} doğrulanamadı: {e}\n")

        self.log.insert(tk.END, "\n🎉 Tüm işlemler tamamlandı.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = GSCApp(root)
    root.mainloop()
