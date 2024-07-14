<script>
    import { onMount } from 'svelte';
    import AssetStats from './components/AssetStats.svelte';
    import SidebarMenu from './components/SidebarMenu.svelte';
    import RecentPayments from './components/RecentPayments.svelte';
    import FavoriteContacts from './components/FavoriteContacts.svelte';
    import TransferHistory from './components/TransferHistory.svelte';

    let showTransferHistory = false;

    function toggleTransferHistory() {
        showTransferHistory = !showTransferHistory;
    }
</script>

<!-- Main Dashboard Layout -->
<div class="dashboard flex flex-col lg:flex-row min-h-screen bg-gradient-to-r from-purple-700 via-purple-800 to-purple-900 text-white">
    <!-- Sidebar for navigation or quick links -->
    <div class="sidebar lg:w-1/4 pl-8 pr-8 pb-8 bg-gradient-to-r from-purple-600 to-purple-700 text-white">
        <div class="mt-10">
            <h2 class="text-4xl font-bold text-white mb-4">My Balance</h2>
            <AssetStats />
        </div>
        <nav class="menu h-full w-80 pl--10 text-3xl text-white">
            
                <SidebarMenu />
            
        </nav>
       
    </div>

    <!-- Main content area -->
    <div class="content flex-1 p-8 bg-white">
        <!-- `RecentPayments` displayed at the top of the dashboard -->
        <div id="recent-payments" class="mb-10">
            
            <div class="recent-payments grid grid-cols-1 gap-6">
                <RecentPayments />
            </div>
            
        </div>

       
    </div>
</div>

<style>
    .dashboard {
        background: #0d011b;
        background-size: cover;
    }

    .sidebar {
        background: linear-gradient(to bottom, #1e293b, 0d011b);
        
    }

    .btn {
        transition: background-color 0.3s, color 0.3s, transform 0.3s;
    }

    .btn:hover {
        transform: scale(1.05);
    }

    .content h2 {
        color: #010101;
    }

    .recent-payments .payment-card {
        background: rgba(0, 0, 0, 0.1);
        padding: 1rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .see-all-btn {
        display: inline-block;
        margin-top: 1rem;
    }
</style>

