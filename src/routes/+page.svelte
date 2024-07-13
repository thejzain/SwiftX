<!-- A modern Hero page for a decentralized exchange on Stellar blockchain with a Web3 style -->
<div class="hero min-h-screen bg-gradient-to-r from-purple-700 via-purple-800 to-purple-900 text-white flex flex-col items-center justify-center text-center px-4 py-16">
    <h1 class="text-6xl font-extrabold mb-4">Welcome to SwiftEx!</h1>
    <p class="mb-8 text-xl">Empowering everyone to use blockchain for borderless, fast, and low-cost money transfers without middlemen.</p>
    <p class="mb-6 text-lg">Sign in with your email and start sending money seamlessly.</p>
    <div data-sveltekit-preload-data="tap" data-sveltekit-preload-code="hover" class="flex flex-col sm:flex-row">
        <a href="/signup" class="btn bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-8 rounded-full mb-4 sm:mb-0 sm:mr-4">Get Started</a>
        <a href="/login" class="btn bg-transparent border-2 border-white text-white font-semibold py-3 px-8 rounded-full hover:bg-white hover:text-indigo-600">Sign In</a>
    </div>
    <div class="mt-10">
        <h2 class="text-3xl font-bold mb-4">Why SwiftEx?</h2>
        <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-8">
            <div class="feature max-w-xs text-left">
                <h3 class="text-2xl font-semibold">Borderless</h3>
                <p>Send and receive money from anywhere in the world without restrictions.</p>
            </div>
            <div class="feature max-w-xs text-left">
                <h3 class="text-2xl font-semibold">Fast</h3>
                <p>Experience lightning-fast transactions powered by the Stellar blockchain.</p>
            </div>
            <div class="feature max-w-xs text-left">
                <h3 class="text-2xl font-semibold">Low-Cost</h3>
                <p>Enjoy low fees and no middlemen, making money transfers more affordable.</p>
            </div>
        </div>
    </div>
</div>

<style>
    .hero {
        background: linear-gradient(135deg, #0d011b, #100722, #3a097b, #24018e, #a733d9, #ce28f8, #f06dff, #cd08cd);
        background-size: 200% 200%;
        animation: gradientAnimation 15s ease infinite;
    }

    @keyframes gradientAnimation {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    .btn {
        transition: background-color 0.3s, color 0.3s, transform 0.3s;
    }

    .btn:hover {
        transform: scale(1.05);
    }
</style>
