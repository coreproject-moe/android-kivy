from jnius import autoclass

GeckoSession = autoclass("org.mozilla.geckoview.GeckoSession")
GeckoRuntime = autoclass("org.mozilla.geckoview.GeckoRuntime")
GeckoView = autoclass("org.mozilla.geckoview.GeckoView")

GeckoSession.setContentDelegate(GeckoSession.ContentDelegate())

PythonActivity = autoclass("org.kivy.android.PythonActivity")

sRuntime = GeckoRuntime.create(PythonActivity)


def get_url(url: str):
    GeckoSession.open(sRuntime)
    GeckoView.setSession(GeckoSession)
    GeckoSession.loadUri(url)
