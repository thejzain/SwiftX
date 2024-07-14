<script lang="ts">
    import TruncatedKey from '$lib/components/TruncatedKey.svelte';
    import { page } from '$app/stores';
    import { transfers } from '$lib/stores/transfersStore';
    import { webAuthStore } from '$lib/stores/webAuthStore';
    import { queryTransfers24 } from '$lib/stellar/sep24';
    import { queryTransfers6 } from '$lib/stellar/sep6';

    let expiredToken = false;

    const protocolBadgeClasses = {
        sep6: 'badge badge-secondary',
        sep24: 'badge badge-accent',
    };

    type Transfer = {
        id: string;
        amount_in: string;
        asset_code: string;
        kind: string;
        protocol: 'sep6' | 'sep24';
        status: string;
        started_at: string;
        stellar_transaction_id?: string;
        more_info_url?: string;
    };

    const query = (protocol: 'sep6' | 'sep24', assetCode: string, homeDomain: string): Promise<Transfer[]> => 
        new Promise((resolve) => {
            const fetchTransfers = protocol === 'sep6' ? queryTransfers6 : queryTransfers24;
            fetchTransfers({
                authToken: $webAuthStore[homeDomain],
                assetCode,
                publicKey: $page.data.publicKey,
                homeDomain,
            }).then(({ transactions }: { transactions: Transfer[] }) =>
                resolve(
                    transactions.map(item => ({
                        ...item,
                        asset_code: assetCode,
                        protocol,
                    }))
                )
            );
        });

    const transfersPromise = async (): Promise<Transfer[]> => {
        let transfersPromises: Promise<Transfer[]>[] = [];
        if ($transfers) {
            for (const homeDomain in $transfers) {
                if ($webAuthStore[homeDomain] && !webAuthStore.isTokenExpired(homeDomain)) {
                    for (const protocol in $transfers[homeDomain]) {
                        const uniqueAssets = [
                            ...new Set(
                                $transfers[homeDomain][protocol].map(item => item.asset_code)
                            ),
                        ];
                        uniqueAssets.forEach(assetCode => {
                            transfersPromises.push(query(protocol as 'sep6' | 'sep24', assetCode, homeDomain));
                        });
                    }
                } else {
                    expiredToken = true;
                }
            }
        }
        const allTransfers = await Promise.all(transfersPromises);
        return allTransfers.flat().sort((a, b) => new Date(b.started_at) - new Date(a.started_at));
    };
</script>

{#if $transfers}
    <h3 class="text-3xl font-bold mb-4">Transfer History</h3>
    <div class="spacer"></div>
    {#await transfersPromise() then allTransfers}
        <table class="table-compact table text-lg">
            <thead>
                <tr class="abc">
                    <th>Amount</th>
                    <th>Asset</th>
                    <th>Direction</th>
                    <th>Protocol</th>
                    <th>Status</th>
                    <th>Date</th>
                    <th>More Info</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {#each allTransfers as transfer (transfer.id)}
                    <tr>
                        <th>{transfer.amount_in}</th>
                        <td>{transfer.asset_code}</td>
                        <td>{transfer.kind}</td>
                        <td>
                            <div class={protocolBadgeClasses[transfer.protocol]}>
                                {transfer.protocol}
                            </div>
                        </td>
                        <td>{transfer.status}</td>
                        <td>{new Date(Date.parse(transfer.started_at)).toLocaleString()}</td>
                        <td>
                            {#if transfer.status === 'completed'}
                                <a target="_blank" href={`https://stellar.expert/explorer/testnet/tx/${transfer.stellar_transaction_id}`}>
                                    View Stellar transaction
                                </a>
                            {:else if 'more_info_url' in transfer}
                                <a target="_blank" href={transfer.more_info_url}>View more info</a>
                            {/if}
                        </td>
                        <td>
                            {#if transfer.kind === 'withdrawal' && transfer.status === 'pending_user_transfer_start'}
                                Start a Payment
                            {:else}
                                Nevermind
                            {/if}
                        </td>
                    </tr>
                {/each}
            </tbody>
        </table>
        {#if expiredToken}
            <p>
                It looks like there may be a problem with some of your anchor authentication. Head over
                to the <a href="/dashboard/transfers">Transfers Page</a> to check that out.
            </p>
        {/if}
    {/await}
{/if}

<style>
    .text-lg {
        font-size: 1.5rem; /* Increase this value to make text larger */
    }
    .text-3xl {
        font-size: 2.25rem; /* Increase this value to make text larger */
    }
    .abc {
        font-size: 1.26rem;
    }
    .spacer {
        margin-bottom: 2rem; /* Adjust the space between heading and table */
    }
</style>
