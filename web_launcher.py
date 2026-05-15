import webbrowser

def open_studio_link():
    """Aapki official Herbalife Smart Wellness Studio website ko open karta hai"""
    url = "https://herbalife-smart-wellness-studio.my.canva.site/page-3"
    try:
        # Default web browser mein link kholega
        webbrowser.open(url, new=2)
        return True
    except Exception as e:
        print(f"Website load karne mein error aaya: {e}")
        return False

# Poore App ko ek sath tie-up karne ke liye master configuration generator
def get_app_metadata():
    return {
        "app_name": "Herbalife Smart Wellness Studio",
        "version": "1.0.0",
        "target_sheets_gid": "339189941",
        "website_url": "https://herbalife-smart-wellness-studio.my.canva.site/page-3"
    }
