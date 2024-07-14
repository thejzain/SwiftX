<!--
@component

The `Navbar` component implements a very simple navigation menu that will be
used on all of the `/dashboard/*` pages a user might interact with. This
includes a link back to the dashboard, as well as the user's SEP-33 identicon,
which is in-turn a menu to see the user's KYC fields and the `/dashboard/dev`
page.

More information about SEP-33 can be found here:
<https://stellar.org/protocol/sep-33>
-->

<script>
    // We import things from external packages that will be needed
    import { MenuIcon } from 'svelte-feather-icons'
    import img from './logo.png'

    // We import any stores we will need to read and/or write
    import { page } from '$app/stores'
</script>

<header class="navbar bg-gradient-to-r from-purple-700 via-purple-800 to-purple-900 text-white">
    <label for="drawer-toggle" class="btn-ghost drawer-button btn-square btn lg:hidden"
        ><MenuIcon size="24" /></label
    >
    <div class="flex-1">
        <a href="/dashboard" class="btn-ghost btn text-4xl normal-case">SwiftX</a>
    </div>
    <div class="relative flex items-center justify-center w-16 h-16">
        <img
            src="https://file.loading.io/resources/icon/kcjcu0.svg"
            alt="Mailbox"
            class="w-12 h-12"
        />
        <span class="absolute top-0 right-0 flex items-center justify-center w-5 h-5 text-xs font-bold text-white bg-red-500 rounded-full">3</span>
    </div>
</header>
<style>
    .relative {
        position: relative;
    }
    .absolute {
        position: absolute;
    }
    .top-0 {
        top: 0;
    }
    .right-0 {
        right: 0;
    }
    .w-5 {
        width: 1.25rem;
    }
    .h-5 {
        height: 1.25rem;
    }
    .text-xs {
        font-size: 0.75rem;
    }
    .font-bold {
        font-weight: 700;
    }
    .text-white {
        color: #fff;
    }
    .bg-red-500 {
        background-color: #f56565;
    }
    .rounded-full {
        border-radius: 9999px;
    }
</style>
