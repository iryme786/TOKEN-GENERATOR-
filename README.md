# Classplus Token Generator API

This Express.js backend generates a login token for Classplus using mobile number and org code.

## 🛠 Setup

```bash
npm install
node server.js
```

### 🔗 POST /token

```json
{
  "mobile": "9876543210",
  "orgCode": "ABCD"
}
```

Returns:

```json
{
  "token": "your_jwt_token_here"
}
```

✅ Host on Render, Vercel or Railway