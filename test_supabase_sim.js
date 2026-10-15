// Simulate browser environment in Node
const mockStorage = {};
global.localStorage = {
    getItem: (k) => mockStorage[k] || null,
    setItem: (k, v) => { mockStorage[k] = v; },
    removeItem: (k) => { delete mockStorage[k]; }
};

global.window = {
    location: {
        origin: 'http://localhost:8080',
        pathname: '/',
        assign: (url) => { console.log('window.location.assign called with:', url); }
    }
};

const https = require('https');
// Fetch Supabase JS bundle and execute
https.get('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2', (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
        // eval bundle in global context
        const vm = require('vm');
        const context = {
            window: global.window,
            localStorage: global.localStorage,
            console: console,
            fetch: global.fetch,
            navigator: { userAgent: 'Node' },
            btoa: (s) => Buffer.from(s).toString('base64'),
            atob: (s) => Buffer.from(s, 'base64').toString(),
            URL: URL,
            URLSearchParams: URLSearchParams,
            crypto: require('crypto').webcrypto
        };
        vm.createContext(context);
        vm.runInContext(data, context);

        const supabase = context.window.supabase;
        console.log('Supabase loaded:', !!supabase);

        const SUPABASE_URL = 'https://tgcgdgmgxjuvwedwcvlf.supabase.co';
        const SUPABASE_ANON_KEY = 'sb_publishable_t_n3odLV8Icio8GY1DqSsg_3-KLku0E';

        const client = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
            auth: {
                persistSession: true,
                detectSessionInUrl: true
            }
        });

        console.log('Client created!');
        client.auth.signInWithOAuth({
            provider: 'google',
            options: {
                redirectTo: 'http://localhost:8080/'
            }
        }).then(res => {
            console.log('signInWithOAuth result:', res);
            console.log('localStorage keys after signInWithOAuth:', Object.keys(mockStorage));
        }).catch(err => {
            console.error('signInWithOAuth error:', err);
        });
    });
});
