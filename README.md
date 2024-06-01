
# Telegram Watermark Bot

A Telegram bot to add customizable watermarks to videos. This bot allows users to add a PNG/JPG/GIF watermark to videos with options to adjust position, size, and quality using interactive buttons.

## Features

- **Interactive Setup**: Use inline buttons to set watermark position, size, and quality.
- **Watermark Formats**: Supports PNG, JPG, and GIF for watermarks.
- **Customizable Settings**: Easily adjust watermark position, size, and video quality.
- **Video Processing**: Uses FFmpeg for efficient video processing.
- **Error Handling**: Informs users about missing steps or errors.

## Bot Commands

- `/start` or `/help`: Get started with instructions and options to set watermark properties.

## Inline Buttons

- **Set Position**: Choose from Top-Left, Top-Right, Bottom-Left, Bottom-Right.
- **Set Size**: Options for 50%, 75%, 100%.
- **Set Quality**: Options for Low, Medium, High.

## Setup and Deployment

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/TG-watermark.git
   cd TG-watermark
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file and add your configuration variables:
   ```plaintext
   BOT_TOKEN=your-bot-token
   API_ID=your-api-id
   API_HASH=your-api-hash
   LOG_CHANNEL=your-log-channel-id
   UPDATES_CHANNEL=your-updates-channel-id
   OWNER_ID=your-owner-id
   ```

5. **Run the bot**:
   ```bash
   python bot.py
   ```

### Docker Deployment

1. **Build the Docker image**:
   ```bash
   docker build -t tg-watermark-bot .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d --env-file .env --name tg-watermark-bot tg-watermark-bot
   ```

### Heroku Deployment

1. **Create a Heroku app**:
   ```bash
   heroku create tg-watermark-bot
   ```

2. **Set Heroku environment variables**:
   ```bash
   heroku config:set BOT_TOKEN=your-bot-token
   heroku config:set API_ID=your-api-id
   heroku config:set API_HASH=your-api-hash
   heroku config:set LOG_CHANNEL=your-log-channel-id
   heroku config:set UPDATES_CHANNEL=your-updates-channel-id
   heroku config:set OWNER_ID=your-owner-id
   ```

3. **Deploy to Heroku**:
   ```bash
   git push heroku main
   ```

## Project Structure

```
TG-watermark/
├── core/
│   ├── __init__.py
│   ├── ffmpeg.py
│   ├── clean.py
├── Procfile
├── README.md
├── app.json
├── bot.py
├── config.env
├── config.py
├── requirements.txt
├── runtime.txt
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project was inspired by [AbirHasan2005/Watermark-Bot](https://github.com/AbirHasan2005/Watermark-Bot).
- Thanks to the contributors of the Pyrogram and FFmpeg projects for their amazing tools.

---

Feel free to customize this `README.md` further to suit your specific needs.
