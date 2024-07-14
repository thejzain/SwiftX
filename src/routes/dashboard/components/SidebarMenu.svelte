

<script>
    // We import any stores we will need to read and/or write
    import { page } from '$app/stores'
    const dashboardRoutes = [
        { route: '/dashboard/contacts', text: 'Friend List' },    
        { route: '/dashboard/send', text: 'Send Money ' },
        
       
    ]
</script>

<ul class="menu h-80 w-80 p-4 text-3xl bg-gradient-to-r from-purple-600 to-purple-700 text-white rounded-lg shadow-lg text-base-content">
    {#each dashboardRoutes as route}
        {@const linkClass = $page.route.id === route.route ? 'active': ''}
        <li>
            <a href={route.route} class={linkClass}
                >{route.text}</a
            >
        </li>
    {/each}
</ul>
