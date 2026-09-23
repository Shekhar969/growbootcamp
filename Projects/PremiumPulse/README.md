# PremiumPulse

## Supabase configuration

The Supabase CDN defines a browser global named `supabase`. The application
does not redeclare that name; it creates the client as `supabaseClient` to avoid
the `Identifier 'supabase' has already been declared` error.

Because this is a static page, a `.env` file is not loaded automatically by the
browser. Define the public project URL and anon key before `script.js` loads:

```html
<script>
    window.SUPABASE_URL = "https://your-project.supabase.co";
    window.SUPABASE_ANON_KEY = "your-anon-key";
</script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="script.js"></script>
```

The page expects a `locations` table with `id` and `name` columns. The anon key
is safe for browser use when Supabase Row Level Security and read policies are
configured for that table.
