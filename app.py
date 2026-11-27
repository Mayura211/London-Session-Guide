import os
import sys
import threading
from pathlib import Path
import webview
from updater import Updater, run_update_helper

class API(Updater):
    def install_update(self, storage_backup):
        result = super().install_update(storage_backup)
        if result['ok']:
            threading.Timer(0.8, webview.windows[0].destroy).start()
        return result

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--apply-update':
        sys.exit(run_update_helper(sys.argv[2:]))
    resource = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent))
    data = Path(os.environ.get('LOCALAPPDATA', str(Path.home()))) / 'LondonSessionGuide'
    data.mkdir(parents=True, exist_ok=True)
    # Use a stable HTML path and WebView profile across installer upgrades.
    html = data / 'index.html'
    html.write_bytes((resource / 'index.html').read_bytes())
    webview.create_window('Forex Backtest Data', str(html), width=1280, height=850,
                          min_size=(850, 600), js_api=API((resource / 'version.txt').read_text().strip()))
    webview.start(private_mode=False, storage_path=str(data / 'WebView'), gui='edgechromium')
