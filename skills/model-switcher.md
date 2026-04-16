# Model Switcher Skill

## Meta
- **Name:** model-switcher
- **Description:** Mengganti model AI yang digunakan oleh bot Telegram
- **Triggers:**
  - "ganti model gemini"
  - "ganti model big pickle"
  - "switch bot to gemini"
  - "switch bot to big pickle"

## Instruction
Jika user meminta untuk mengganti model bot, jalankan script PowerShell berikut dengan parameter yang sesuai:
`powershell -ExecutionPolicy Bypass -File "C:\Users\USER\.config\opencode\switch-bot-model.ps1" -TargetModel [model_name]`

Berikan konfirmasi kepada user setelah bot berhasil direstart.
