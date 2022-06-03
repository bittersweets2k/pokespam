from webserver import keep_alive
import requests

channelID = PUT THE CHANNEL ID
headers = {
    "authorization":
    "Njc5NDExMzAwNTAxMjkxMDI4.GFLC4s.paHp_aryW__OKri0hIcGWg0lVleYFTc-Z-iXLM"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{816575039633752114}/messages",
            headers=headers,
            json={"content": line})
