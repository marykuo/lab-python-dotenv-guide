from config import settings


def main():
    print("=== env ===")
    print(f"App Name (APP_NAME): {settings.APP_NAME}")
    print(f"API Host (API_HOST): {settings.API_HOST}")
    print(f"API Key (API_KEY)  : {settings.API_KEY}")


if __name__ == "__main__":
    main()
