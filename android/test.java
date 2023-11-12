import ;
import ;
import ;

GeckoView view = findViewById(R.id.geckoview);
GeckoSession session = new GeckoSession();

// Workaround for Bug 1758212


if (sRuntime == null) {
  // GeckoRuntime can only be initialized once per process
  sRuntime = GeckoRuntime.create(this);
}
