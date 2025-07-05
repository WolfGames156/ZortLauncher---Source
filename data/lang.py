import json, locale
import os, sys
import variables

if sys.platform == 'win32':
    platform = ".exe"
elif sys.platform == 'linux':
    platform = ".bin"

lang_codes = ["en", "tr", "fr"]

# Load the system language
os.makedirs(f'{variables.app_directory}/config', exist_ok=True)
if os.path.exists(f'{variables.app_directory}/config/config.json'):
    with open(f'{variables.app_directory}/config/config.json', 'r') as f:
        try:
            config = json.load(f)
            current_language = config.get('lang')
            if current_language not in lang_codes:
                current_language = "tr"
                config["lang"] = current_language
                with open(f'{variables.app_directory}/config/config.json', 'w') as f:
                    json.dump(config, f, indent=4)
        except json.JSONDecodeError:
            current_language = "tr"
else:
    current_language = locale.getdefaultlocale()[0].split('_')[0]
    if current_language not in lang_codes:
        current_language = "tr"
    
    

languages = {
    "en": {
        "language": "Select Language",
        "available_languages": {
            "en": "English",
            "tr": "Turkish",
            "fr": "French",
        },
        "launcher_name": "ZortLauncher",
        "launcher_title": "ZortLauncher for Minecraft",
        "label_username": "By WolfGames\nWelcome to ZortLauncher\nEnter your username",
        "user_placeholder": "Enter your username (Steve)",
        "checkbox_snapshots": "Show snapshots",
        "btn_install_minecraft": "Install Minecraft",
        "btn_install_loader": "Install Fabric",
        "btn_play": "Play",
        "btn_mod_manager": "Mod Manager",
        "btn_shorts": "Shortcuts",
        "get_started": "Get Started",
        "welcome": "Welcome to ZortLauncher!",
        "welcome_message": (
    "ZortLauncher is a Minecraft launcher that allows you to install and play the version you want, "
    "created with Python and Qt for the GUI.<br>"
    "To get started, you can install the Minecraft version you want, install Fabric or Forge, and play the game. "
    "You can also manage your mods with the Mod Manager and enable Discord Rich Presence.<br><br>"
    f"my other projects: <a style='color: #00aaff;' href='{variables.website_url2}'>Zoream</a>.<br><br>"
    "ZortLauncher offers some features like:"
    "<ul>"
    "<li>Install Minecraft versions</li>"
    "<li>Install Fabric and Forge</li>"
    "<li>Play the Minecraft version you want</li>"
    "<li>Enable Discord Rich Presence</li>"
    "<li>Multilanguage support</li>"
    "</ul>"
),
        "install_themes": "Install Theme",

        "dont_show_again": "Don't show this message again",
        "close": "Close",
        "open_website": "ZortLauncher Web Site",
        "open_launcher_directory": "Open Application Directory",
        "open_minecraft_directory": "Open Minecraft Directory",
        "save": "Save changes",
        "discord_rpc": "Enable Discord Rich Presence",
        "jvm_tip": "Leave blank and save to reset to default",
        "label_jvm_args": "JVM arguments (Expert settings)",
        "settings": "Settings",
        "install": "Install",
        "info_label_minecraft": "Install the version of Minecraft you want",
        "info_label_loader": "Install the latest available version of Fabric for the desired Minecraft version",
        "loader_label": "Select the loader version",
        "no_internet": "No internet connection",
        "no_username": "Please enter your user name",
        "java_not_installed": "Java is not installed",
        "java_not_installed_linux": "Please install Java to run Minecraft.\n\nFor example, in Ubuntu you can install it with the command 'sudo apt install default-jre'",
        "java_not_installed_win": "It's necessary to install Java to run Minecraft, please install it and restart the launcher",
        "ask_install_java": "Java is not installed. Do you want to open the download page?",
        "no_versions_installed": "No versions installed",
        "forge_installed": "Forge 1.0 has been installed successfully",
        "forge_not_found": "No Forge version found for this version of Minecraft",
        "forge_installation": "Forge for Minecraft 1.0 will be installed, this may take a few minutes depending on your internet connection, please wait...",
        "minecraft_installed": "Minecraft 1.0 has been installed successfully",
        "minecraft_installation": "Minecraft 1.0 will be installed, this may take a few minutes depending on your internet connection, please wait...",
        "login_microsoft": "Login with Microsoft",
        "relogin_microsoft": "Reauthenticate with Microsoft",
        "logout_microsoft": "Logout",
        "microsoft_account_not_found": "Minecraft Java Edition Not Found",
        "microsoft_account_not_found_desc": "It looks like your account doesn't have Minecraft Java Edition. Would you like to visit the official Minecraft website to buy it?",
        "token_expired": "Your session has expired, you need to login again, do you want to login now?",
        "logged_as": "Welcome to ZortLauncher\n\nLogged in as",
        "theme_ask": "Multiple themes were found, which may cause issues. Would you like to open the plugins directory to remove the additional themes?",
        "theme_error": "The first detected theme will be attempted for loading, please remove additional themes to prevent issues.",
        "discord_error": "Could not connect to Discord Rich Presence, ensure that Discord is running",
        "mod_manager_title": "Mod Manager",
        "mod_manager_info": "The Mod Manager renames mods with the game version. Ex: 'mod.jar' to 'VERSION_TEXT_mod.jar'. To install, drag the file or click 'Install mod' (.jar and .olpkg). 'olpkg' files are disabled mods that you can activate.",
        "mod_manager_disabled": "The Mod Manager is disabled because no compatible version is detected.\nPlease select a valid (Forge, Fabric, Quilt, NeoForge) version in the launcher settings.",
        "active_mods": "Active Mods",
        "inactive_mods": "Inactive Mods",
        "mod_already_exists": "The mod already exists in the list of mods",
        "file_exists": "The file already exists. Do you want to overwrite it?",
        "invalid_file_format": "Invalid file format only .jar and .olpkg files are supported",
        "btn_activate": "Activate mod",
        "btn_install": "Install mod",
        "btn_deactivate": "Deactivate mod",
        "btn_open_mods_dir": "Open Mods Directory",
        "error_no_version": "First install a version to manage mods",
        "auth_window_title": "Microsoft Authentication",
        "auth_window_label": "Please wait while we authenticate you with Microsoft...",
        "auth_success": "Authentication Successful - You can close this window now.",
        "auth_failure": "Authentication Failed - Please try again.",
        "restart_app": "The application needs to restart to apply the changes, do you want to close it now?, you will have to open it manually.",
        "shortcuts": "Shortcuts",
        "shortcuts_info": (
            "You can create shortcuts to launch the game with different configurations. "
            "For example, you can create a shortcut to launch the game with a specific Minecraft version. "
            f"Use the following format: 'ZortLauncher{platform} -mc_ver 1.0 -mc_name Steve', where '1.0' is the Minecraft version and 'Steve' is the username. "
            f"For more information, visit the <a style='color: #00aaff;' href='{variables.website_url}/guide'>ZortLauncher documentation</a>.<br><br>"
            "Example of a shortcut to launch the game with version 1.0 and username Steve:<br>"
            f"<b>'ZortLauncher{platform} -mc_ver 1.0 -mc_name Steve'</b><br><br>"
            f"Use <b>'ZortLauncher{platform} -h'</b> to see the available parameters."
        ),
        "logout_success": "You have successfully logged out",
        "copy_parameters": "Copy parameters",
        "parameters_copied": "Success",
        "parameters_copied_info": "The parameters have been copied to the clipboard, you can add them to the game shortcut",
        "offline_mode": "Offline mode",
        "offline_mode_error": "If you want to play in offline mode, you must enter a username",
        "no_refresh_token": "You must be logged in to use the online mode, please run ZortLauncher without arguments to open the GUI and log in",
        "no_version": "No version has been selected, please run ZortLauncher -mc_ver <version> -mc_name <username> -online <true/false> to run Minecraft",
        "mc_fail": "An error occurred while trying to run Minecraft please run ZortLauncher without arguments to open the GUI",
        "ask_update": "Check for updates",
        "update_available": "An update is available, do you want to download it?",
        "downloading": "Downloading...",
        "download_format": "Select Download Format",
        "select_folder": "Please select the download location.",
        "download_cancelled": "Download cancelled.",
        "download_success": "The download has been completed successfully.",
        "open_bin": "You can open the .bin file using the command './dest' or open it using the file manager.",
        "xterm_not_found": "The automatic installation of the .deb file has failed. Please install it manually using the command 'sudo dpkg -i dest'",
        "update_complete": "The update has been installed successfully.",
        "error_occurred": "An error occurred: ",
        "microsoft_login_title": "Login with Microsoft",
        "ask_logout_title": "Logout",
        "ask_logout_desc": "Are you sure you want to log out? If you log out, you will need to log in again to play with your Microsoft account.",
        "invalid_username": "Invalid username, must be between 3 and 16 characters and not contain spaces or special characters",
        "work_in_progress": "Work in progress",
        "work_in_progress_info": "This feature is not yet available, but will be available in future updates.",
    },
    "tr": {
    "language": "Dil Seçin",
    "available_languages": {
        "en": "İngilizce",
        "tr": "Türkçe",
        "fr": "Fransızca",
    },
    "launcher_name": "ZortLauncher",
    "launcher_title": "Minecraft için ZortLauncher",
    "label_username": "By WolfGames\nZortLauncher'a hoş geldiniz\nKullanıcı adınızı girin",
    "user_placeholder": "Kullanıcı adınızı girin (Steve)",
    "checkbox_snapshots": "Snapshots göster",
    "btn_install_minecraft": "Minecraft'ı Yükle",
    "btn_install_loader": "Fabric'i Yükle",
    "btn_play": "Oyna",
    "btn_mod_manager": "Mod Yöneticisi",
    "btn_shorts": "Kısayollar",
    "get_started": "Başlayalım",
    "welcome": "ZortLauncher'a Hoş Geldiniz!",
    "welcome_message": (
    "ZortLauncher, istediğiniz Minecraft sürümünü yükleyip oynayabileceğiniz bir launcher'dır, "
    "Python ve Qt ile GUI olarak geliştirilmiştir.<br>"
    "Başlamak için istediğiniz Minecraft sürümünü yükleyebilir, Fabric veya Forge'u kurup oyunu oynayabilirsiniz. "
    "Ayrıca Mod Yöneticisi ile modlarınızı yönetebilir ve Discord Rich Presence'i etkinleştirebilirsiniz.<br><br>"
    f"Diğer Projelerim: <a style='color: #00aaff;' href='{variables.website_url2}'>Zoream</a><br><br>"
    "ZortLauncher şu özellikleri sunar:"
    "<ul>"
    "<li>Minecraft sürümlerini yükleyebilme</li>"
    "<li>Fabric ve Forge yükleyebilme</li>"
    "<li>İstediğiniz Minecraft sürümünü oynayabilme</li>"
    "<li>Discord Rich Presence'i etkinleştirebilme</li>"
    "<li>Çoklu dil desteği</li>"
    "</ul>"
),

    "dont_show_again": "Bu mesajı tekrar gösterme",
    "close": "Kapat",
    "open_website": "ZortLauncher Web Site",
    "open_launcher_directory": "Uygulama Dizini'ni Aç",
    "open_minecraft_directory": "Minecraft Dizini'ni Aç",
    "save": "Değişiklikleri Kaydet",
    "discord_rpc": "Discord Rich Presence'i Etkinleştir",
    "jvm_tip": "Varsayılan ayarlara dönmek için boş bırakıp kaydedin",
    "label_jvm_args": "JVM argümanları (Uzman ayarları)",
    "settings": "Ayarlar",
    "install": "Yükle",
    "info_label_minecraft": "İstediğiniz Minecraft sürümünü yükleyin",
    "info_label_loader": "İstediğiniz Minecraft sürümü için mevcut en son Fabric sürümünü yükleyin",
    "loader_label": "Loader sürümünü seçin",
    "no_internet": "İnternet bağlantısı yok",
    "no_username": "Lütfen kullanıcı adınızı girin",
    "java_not_installed": "Java yüklü değil",
    "java_not_installed_linux": "Minecraft'ı çalıştırmak için Java'yı yükleyin.\n\nÖrneğin, Ubuntu'da 'sudo apt install default-jre' komutuyla yükleyebilirsiniz",
    "java_not_installed_win": "Minecraft'ı çalıştırmak için Java yüklenmelidir, lütfen yükleyin ve launcher'ı yeniden başlatın",
    "ask_install_java": "Java yüklü değil. İndirme sayfasını açmak ister misiniz?",
    "no_versions_installed": "Yüklü sürüm yok",
    "forge_installed": "Forge 1.0 başarıyla yüklendi",
    "forge_not_found": "Bu Minecraft sürümü için Forge bulunamadı",
    "forge_installation": "Minecraft 1.0 için Forge yüklenecek, internet hızınıza bağlı olarak birkaç dakika sürebilir, lütfen bekleyin...",
    "minecraft_installed": "Minecraft 1.0 başarıyla yüklendi",
    "minecraft_installation": "Minecraft 1.0 yüklenecek, internet hızınıza bağlı olarak birkaç dakika sürebilir, lütfen bekleyin...",
    "login_microsoft": "Microsoft ile giriş yap",
    "relogin_microsoft": "Microsoft ile yeniden kimlik doğrula",
    "logout_microsoft": "Çıkış yap",
    "microsoft_account_not_found": "Minecraft Java Edition bulunamadı",
    "microsoft_account_not_found_desc": "Hesabınızda Minecraft Java Edition görünmüyor. Satın almak için resmi Minecraft web sitesini ziyaret etmek ister misiniz?",
    "token_expired": "Oturumunuz süresi doldu, tekrar giriş yapmanız gerekiyor, şimdi giriş yapmak ister misiniz?",
    "logged_as": "ZortLauncher'a hoş geldiniz\n\nGiriş yapılan kullanıcı",
    "theme_ask": "Birden fazla tema bulundu, bu sorunlara yol açabilir. Ek temaları kaldırmak için eklenti dizinini açmak ister misiniz?",
    "theme_error": "İlk bulunan tema yüklenmeye çalışılacak, sorun yaşamamak için ek temaları kaldırın.",
    "discord_error": "Discord Rich Presence'e bağlanılamadı, Discord'un çalıştığından emin olun",
    "mod_manager_title": "Mod Yöneticisi",
    "mod_manager_info": "Mod Yöneticisi, modları oyun sürümüne göre yeniden adlandırır. Örnek: 'mod.jar' -> 'VERSION_TEXT_mod.jar'. Mod yüklemek için dosyayı sürükleyin veya 'Mod yükle'ye tıklayın (.jar ve .olpkg). 'olpkg' dosyaları devre dışı modlardır, aktif edilebilir.",
    "mod_manager_disabled": "Mod Yöneticisi kapalı çünkü uyumlu sürüm algılanamadı.\nLütfen launcher ayarlarından geçerli (Forge, Fabric, Quilt, NeoForge) sürümü seçin.",
    "active_mods": "Aktif Modlar",
    "inactive_mods": "Pasif Modlar",
    "mod_already_exists": "Mod zaten listede mevcut",
    "file_exists": "Dosya zaten var. Üzerine yazmak ister misiniz?",
    "invalid_file_format": "Geçersiz dosya formatı, sadece .jar ve .olpkg desteklenir",
    "btn_activate": "Modu etkinleştir",
    "btn_install": "Mod yükle",
    "btn_deactivate": "Modu devre dışı bırak",
    "btn_open_mods_dir": "Modlar Dizini'ni Aç",
    "error_no_version": "Modları yönetmek için önce sürüm yükleyin",
    "auth_window_title": "Microsoft Doğrulaması",
    "auth_window_label": "Microsoft ile kimlik doğrulamanız bekleniyor...",
    "auth_success": "Kimlik doğrulama başarılı - Şimdi bu pencereyi kapatabilirsiniz.",
    "auth_failure": "Kimlik doğrulama başarısız - Lütfen tekrar deneyin.",
    "restart_app": "Değişikliklerin uygulanması için uygulama yeniden başlatılmalı, şimdi kapatmak ister misiniz? Manuel açmanız gerekecek.",
    "shortcuts": "Kısayollar",
    "shortcuts_info": (
        "Farklı ayarlarla oyunu başlatmak için kısayollar oluşturabilirsiniz. "
        "Örneğin, belirli bir Minecraft sürümü ile oyun başlatma kısayolu oluşturabilirsiniz. "
        f"Aşağıdaki formatı kullanın: 'ZortLauncher{platform} -mc_ver 1.0 -mc_name Steve', burada '1.0' Minecraft sürümü, 'Steve' kullanıcı adıdır. "
        f"Daha fazla bilgi için <a style='color: #00aaff;' href='{variables.website_url}/guide'>ZortLauncher dökümantasyonunu</a> ziyaret edin.<br><br>"
        "Örnek: 1.0 sürümü ve Steve kullanıcı adı ile oyunu başlatmak için:<br>"
        f"<b>'ZortLauncher{platform} -mc_ver 1.0 -mc_name Steve'</b><br><br>"
        f"Kullanılabilir parametreleri görmek için <b>'ZortLauncher{platform} -h'</b> komutunu kullanın."
    ),
    "logout_success": "Başarıyla çıkış yaptınız",
    "install_themes": "Tema Yükle",

    "copy_parameters": "Parametreleri kopyala",
    "parameters_copied": "Başarılı",
    "parameters_copied_info": "Parametreler panoya kopyalandı, oyun kısayoluna ekleyebilirsiniz",
    "offline_mode": "Çevrimdışı mod",
    "offline_mode_error": "Çevrimdışı modda oynamak için kullanıcı adı girilmelidir",
    "no_refresh_token": "Çevrimiçi modu kullanmak için giriş yapmalısınız, lütfen GUI'yi açıp giriş yapın",
    "no_version": "Sürüm seçilmedi, Minecraft'ı çalıştırmak için ZortLauncher -mc_ver <sürüm> -mc_name <kullanıcı> -online <true/false> komutunu kullanın",
    "mc_fail": "Minecraft çalıştırılırken hata oluştu, GUI'yi açmak için ZortLauncher'ı argümansız çalıştırın",
    "ask_update": "Güncellemeleri kontrol et",
    "update_available": "Güncelleme mevcut, indirmek ister misiniz?",
    "downloading": "İndiriliyor...",
    "download_format": "İndirme Formatını Seçin",
    "select_folder": "Lütfen indirme konumunu seçin.",
    "download_cancelled": "İndirme iptal edildi.",
    "download_success": "İndirme başarıyla tamamlandı.",
    "open_bin": ".bin dosyasını './dest' komutuyla veya dosya yöneticisi ile açabilirsiniz.",
    "xterm_not_found": ".deb dosyasının otomatik kurulumu başarısız oldu. 'sudo dpkg -i dest' komutuyla manuel yükleyin",
    "update_complete": "Güncelleme başarıyla yüklendi.",
    "error_occurred": "Hata oluştu: ",
    "microsoft_login_title": "Microsoft ile giriş yap",
    "ask_logout_title": "Çıkış yap",
    "ask_logout_desc": "Çıkış yapmak istediğinizden emin misiniz? Çıkış yaparsanız Microsoft hesabınızla tekrar giriş yapmanız gerekir.",
    "invalid_username": "Geçersiz kullanıcı adı, 3-16 karakter arasında olmalı, boşluk ve özel karakter içeremez",
    "work_in_progress": "Çalışma devam ediyor",
    "work_in_progress_info": "Bu özellik henüz kullanıma hazır değil, gelecek güncellemelerde eklenecektir.",
},

    "fr": {
        "language": "Sélectionnez la langue",
        "available_languages": {
            "en": "Anglais",
            "tr": "Turkish",
            "fr": "Français",
        },
        "launcher_name": "ZortLauncher",
        "launcher_title": "ZortLauncher pour Minecraft",
        "label_username": "By WolfGames\nBienvenue sur ZortLauncher\nEntrez votre nom d'utilisateur",
        "user_placeholder": "Entrez votre nom d'utilisateur (Steve)",
        "checkbox_snapshots": "Afficher les snapshots",
        "btn_install_minecraft": "Installer Minecraft",
        "btn_install_loader": "Installer Fabric",
        "install_themes": "Installer le Theme",

        "btn_play": "Jouer",
        "btn_mod_manager": "Gestionnaire de Mods",
        "btn_shorts": "Raccourcis",
        "get_started": "Commencer",
        "welcome": "Bienvenue sur ZortLauncher !",
        "welcome_message": (
    "ZortLauncher est un lanceur Minecraft qui vous permet d'installer et de jouer à la version que vous souhaitez, "
    "créé avec Python et Qt pour l'interface graphique.<br>"
    "Pour commencer, vous pouvez installer la version de Minecraft que vous souhaitez, installer Fabric ou Forge et jouer au jeu. "
    "Vous pouvez également gérer vos mods avec le Mod Manager et activer Discord Rich Presence.<br><br>"
    f"mes autres projets : <a style='color: #00aaff;' href='{variables.website_url2}'>Zoream</a>.<br><br>"
    "ZortLauncher propose les fonctionnalités suivantes :"
    "<ul>"
    "<li>Installer des versions de Minecraft</li>"
    "<li>Installer Fabric et Forge</li>"
    "<li>Jouer à la version de Minecraft que vous souhaitez</li>"
    "<li>Activer Discord Rich Presence</li>"
    "<li>Support multilingue</li>"
    "</ul>"
),

        "dont_show_again": "Ne plus afficher ce message",
        "close": "Fermer",
        "open_website": "ZortLauncher Web Site",
        "open_launcher_directory": "Ouvrir le répertoire de l'application",
        "open_minecraft_directory": "Ouvrir le répertoire de Minecraft",
        "save": "Enregistrer les modifications",
        "discord_rpc": "Activer Discord Rich Presence",
        "jvm_tip": "Laissez vide et enregistrez pour réinitialiser aux valeurs par défaut",
        "label_jvm_args": "Arguments JVM (Paramètres avancés)",
        "settings": "Paramètres",
        "install": "Installer",
        "info_label_minecraft": "Installer la version de Minecraft que vous souhaitez",
        "info_label_loader": "Installer la dernière version disponible de Fabric pour la version de Minecraft souhaitée",
        "loader_label": "Sélectionnez la version du loader",
        "no_internet": "Pas de connexion internet",
        "no_username": "Veuillez entrer votre nom d'utilisateur",
        "java_not_installed": "Java n'est pas installé",
        "java_not_installed_linux": "Veuillez installer Java pour exécuter Minecraft.\n\nPar exemple, sur Ubuntu, vous pouvez l'installer avec la commande 'sudo apt install default-jre'",
        "java_not_installed_win": "Il est nécessaire d'installer Java pour exécuter Minecraft, veuillez l'installer et redémarrer le lanceur",
        "ask_install_java": "Java n'est pas installé. Voulez-vous ouvrir la page de téléchargement ?",
        "no_versions_installed": "Aucune version installée",
        "forge_installed": "Forge 1.0 a été installé avec succès",
        "forge_not_found": "Aucune version de Forge trouvée pour cette version de Minecraft",
        "forge_installation": "Forge pour Minecraft 1.0 sera installé, cela peut prendre quelques minutes en fonction de votre connexion internet, veuillez patienter...",
        "minecraft_installed": "Minecraft 1.0 a été installé avec succès",
        "minecraft_installation": "Minecraft 1.0 sera installé, cela peut prendre quelques minutes en fonction de votre connexion internet, veuillez patienter...",
        "login_microsoft": "Connexion avec Microsoft",
        "relogin_microsoft": "Réauthentifier avec Microsoft",
        "logout_microsoft": "Déconnexion",
        "microsoft_account_not_found": "Minecraft Java Edition introuvable",
        "microsoft_account_not_found_desc": "Il semble que votre compte n'a pas Minecraft Java Edition. Souhaitez-vous visiter le site web officiel de Minecraft pour l'acheter ?",
        "token_expired": "Votre session a expiré, vous devez vous reconnecter, voulez-vous vous connecter maintenant ?",
        "logged_as": "Bienvenue sur ZortLauncher\n\nConnecté en tant que",
        "theme_ask": "Plusieurs thèmes ont été trouvés, ce qui peut causer des problèmes. Souhaitez-vous ouvrir le répertoire des plugins pour supprimer les thèmes supplémentaires ?",
        "theme_error": "Le premier thème détecté sera tenté pour le chargement, veuillez supprimer les thèmes supplémentaires pour éviter les problèmes.",
        "discord_error": "Impossible de se connecter à Discord Rich Presence, assurez-vous que Discord est en cours d'exécution",
        "mod_manager_title": "Gestionnaire de Mods",
        "mod_manager_info": "Le Mod Manager renomme les mods avec la version du jeu. Ex : 'mod.jar' en 'VERSION_TEXT_mod.jar'. Pour installer, faites glisser le fichier ou cliquez sur 'Installer mod' (.jar et .olpkg). Les fichiers 'olpkg' sont des mods désactivés que vous pouvez activer.",
        "mod_manager_disabled": "Le Mod Manager est désactivé car aucune version compatible n'est détectée.\nVeuillez sélectionner une version valide (Forge, Fabric, Quilt, NeoForge) dans les paramètres du lanceur.",
        "active_mods": "Mods Actifs",
        "inactive_mods": "Mods Inactifs",
        "mod_already_exists": "Le mod existe déjà dans la liste des mods",
        "file_exists": "Le fichier existe déjà. Voulez-vous l'écraser ?",
        "invalid_file_format": "Format de fichier invalide seuls les fichiers .jar et .olpkg sont pris en charge",
        "btn_activate": "Activer mod",
        "btn_install": "Installer mod",
        "btn_deactivate": "Désactiver mod",
        "btn_open_mods_dir": "Ouvrir le répertoire des mods",
        "error_no_version": "Installez d'abord une version pour gérer les mods",
        "auth_window_title": "Authentification Microsoft",
        "auth_window_label": "Veuillez patienter pendant que nous vous authentifions avec Microsoft...",
        "auth_success": "Authentification réussie - Vous pouvez fermer cette fenêtre maintenant.",
        "auth_failure": "Échec de l'authentification - Veuillez réessayer.",
        "restart_app": "L'application doit redémarrer pour appliquer les modifications, voulez-vous la fermer maintenant ? Vous devrez l'ouvrir manuellement.",
        "shortcuts": "Raccourcis",
        "shortcuts_info": (
            "Vous pouvez créer des raccourcis pour lancer le jeu avec différentes configurations. "
            "Par exemple, vous pouvez créer un raccourci pour lancer le jeu avec une version spécifique de Minecraft. "
            f"Utilisez le format suivant : 'ZortLauncher{platform} -mc_ver 1.0 -mc_name Steve', où '1.0' est la version de Minecraft et 'Steve' est le nom d'utilisateur. "
            f"Pour plus d'informations, visitez la <a style='color: #00aaff;' href='{variables.website_url}/guide'>documentation ZortLauncher</a>.<br><br>"
            "Exemple de raccourci pour lancer le jeu avec la version 1.0 et le nom d'utilisateur Steve :<br>"
            f"<b>'ZortLauncher{platform} -mc_ver 1.0 -mc_name Steve'</b><br><br>"
            f"Utilisez <b>'ZortLauncher{platform} -h'</b> pour voir les paramètres disponibles."
        ),
        "logout_success": "Vous avez bien été déconnecté",
        "copy_parameters": "Copier les paramètres",
        "parameters_copied": "Succès",
        "parameters_copied_info": "Les paramètres ont été copiés dans le presse-papiers, vous pouvez les ajouter au raccourci du jeu",
        "offline_mode": "Mode hors ligne",
        "offline_mode_error": "Si vous souhaitez jouer en mode hors ligne, vous devez entrer un nom d'utilisateur",
        "no_refresh_token": "Vous devez être connecté pour utiliser le mode en ligne, veuillez exécuter ZortLauncher sans arguments pour ouvrir l'interface graphique et vous connecter",
        "no_version": "Aucune version n'a été sélectionnée, veuillez exécuter ZortLauncher -mc_ver <version> -mc_name <username> -online <true/false> pour exécuter Minecraft",
        "mc_fail": "Une erreur s'est produite lors de l'essai d'exécution de Minecraft, veuillez exécuter ZortLauncher sans arguments pour ouvrir l'interface graphique",
        "ask_update": "Vérifier les mises à jour",
        "update_available": "Une mise à jour est disponible, voulez-vous la télécharger ?",
        "downloading": "Téléchargement...",
        "download_format": "Sélectionner le format de téléchargement",
        "select_folder": "Veuillez sélectionner l'emplacement du téléchargement.",
        "download_cancelled": "Téléchargement annulé.",
        "download_success": "Le téléchargement a été effectué avec succès.",
        "open_bin": "Vous pouvez ouvrir le fichier .bin en utilisant la commande './dest' ou l'ouvrir en utilisant le gestionnaire de fichiers.",
        "xterm_not_found": "L'installation automatique du fichier .deb a échoué. Veuillez l'installer manuellement en utilisant la commande 'sudo dpkg -i dest'",
        "update_complete": "La mise à jour a été installée avec succès.",
        "error_occurred": "Une erreur s'est produite : ",
        "microsoft_login_title": "Connexion avec Microsoft",
        "ask_logout_title": "Déconnexion",
        "ask_logout_desc": "Êtes-vous sûr de vouloir vous déconnecter ? Si vous vous déconnectez, vous devrez vous reconnecter pour jouer avec votre compte Microsoft.",
        "invalid_username": "Nom d'utilisateur invalide, doit contenir entre 3 et 16 caractères et ne doit pas contenir d'espaces ou de caractères spéciaux",
        "work_in_progress": "Travail en cours",
        "work_in_progress_info": "Cette fonctionnalité n'est pas encore disponible, mais le sera dans les prochaines mises à jour.",
    }
}

# Function to get the language string
def lang(lang_code, key):
    return languages.get(lang_code, "en").get(key, key)

def change_language(lang_code="en"):
    global current_language
    current_language = lang_code
    config_path = os.path.join(variables.app_directory, 'config/config.json').replace('\\', '/')
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    
    # Read the config.json file if it exists
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError:
                config = {}
    else:
        config = {}

    # Update the language code in the config dictionary
    config["lang"] = lang_code

    # Write the updated config dictionary to the config.json file
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)