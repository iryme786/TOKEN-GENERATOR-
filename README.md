# ClassPlus OTP Token Generator API

## 🔧 Endpoints

### POST `/send-otp`
```json
{
  "orgCode": "ORG123",
  "phoneNumber": "9999999999"
}
```

### POST `/verify-otp`
```json
{
  "orgCode": "ORG123",
  "phoneNumber": "9999999999",
  "otp": "123456"
}
```

---

## 🟢 One-Click Deploy

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://dashboard.render.com/deploy?repo=https://github.com/yourusername/classplus-api)
