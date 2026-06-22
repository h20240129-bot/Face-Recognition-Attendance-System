# Cloudflare Tunnel Based Remote Dashboard Access

## Objective

Provide secure remote access to the Face Recognition Attendance Dashboard without requiring public IP configuration or router port forwarding.

---
 Overview

To enable attendance monitoring from any device, Cloudflare Tunnel was used to expose the locally hosted Flask dashboard to the internet.

This allows authorized users to access the dashboard through a public URL from:

- Mobile Phones
- Laptops
- Tablets
- Desktop Systems

The dashboard remains connected to the centralized attendance database and displays real-time attendance records.

---

## Architecture

Employee Face Recognition
        ↓
Attendance Record Generated
        ↓
Centralized Database
        ↓
Flask Dashboard (localhost:5000)
        ↓
Cloudflare Tunnel
        ↓
Public URL
        ↓
Any Device Browser

---

## Flask Configuration

The Flask application was configured to listen on all network interfaces.

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

This enables external access through the Cloudflare Tunnel.

---

## Running the Dashboard

Start the Flask application:

```powershell
python app.py
```

---

## Creating Cloudflare Tunnel

Open a second terminal and execute:

```powershell
& "C:\Program Files (x86)\cloudflared\cloudflared.exe" tunnel --url http://localhost:5000
```

Cloudflare automatically generates a public URL and maps it to the local Flask server.

---

## Generated Public URL

Example URL:

```text
https://teams-thickness-namespace-mechanism.trycloudflare.com
```

Users can open this URL from any internet-connected device to access the attendance dashboard.

---


<img width="1279" height="664" alt="image" src="https://github.com/user-attachments/assets/70158d18-861a-441f-aa96-1b5f98d48784" />


## Features

### Remote Dashboard Access

- Access attendance records from anywhere.
- No VPN required.
- No router configuration required.

### Real-Time Monitoring

- New attendance records appear automatically.
- Dashboard reads directly from the centralized database.

### Multi-Device Support

Supported devices:

- Android
- iPhone
- Windows
- Linux
- macOS
- Tablets

### Secure Tunnel

Cloudflare Tunnel provides encrypted communication between users and the local dashboard server.

---

## Benefits

- Quick deployment
- No public IP requirement
- No port forwarding
- Easy sharing through URL
- Real-time attendance visibility
- Cross-device accessibility

---

## Result

The Face Recognition Attendance Dashboard was successfully exposed to the internet using Cloudflare Tunnel. Attendance records stored in the centralized database can now be viewed remotely through a browser link from any authorized device.
