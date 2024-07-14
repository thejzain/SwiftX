<script>
    import { Trash2Icon, UserPlusIcon } from 'svelte-feather-icons';
    import TruncatedKey from '$lib/components/TruncatedKey.svelte';
    import { contacts } from '$lib/stores/contactsStore';

    $: newContact = {
        name: '',
        address: '',
        favorite: false,
        id: '',
    };
</script>

<div class="flex min-h-screen bg-gradient-to-r from-purple-700 via-purple-800 to-purple-900 text-white">
    <!-- Left Panel -->
    <div class="w-1/4 p-8 bg-black-800 flex flex-col justify-start">
        <h1 class="text-4xl font-bold mb-4">Friends List</h1>
        <p class="mb-6 text-lg">
            Your Friends list: Organize and manage your money transfer recipients easily.
        </p>
    </div>

    <!-- Right Panel -->
    <div class="flex-1 p-8 bg-white text-black">
        <h3 class="text-3xl font-semibold mb-4">All Friends</h3>

        <div class="overflow-x-auto">
            <table class="table-auto w-full shadow-md rounded-lg overflow-hidden">
                <thead class="bg-gradient-to-r from-purple-600 to-purple-700 text-white">
                    <tr>
                        <th class="w-1/12 text-center p-4">Favorite</th>
                        <th class="p-4">Name</th>
                        <th class="p-4">Address</th>
                        <th class="w-1/12 text-center p-4">Action</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    <tr class="bg-gray-50 hover:bg-gray-100 transition">
                        <th class="text-center">
                            <input
                                bind:checked={newContact.favorite}
                                id="favorite"
                                name="favorite"
                                type="checkbox"
                                class="checkbox-accent checkbox checkbox-sm"
                            />
                        </th>
                        <td class="p-4">
                            <input
                                bind:value={newContact.name}
                                id="name"
                                name="name"
                                type="text"
                                placeholder="Name"
                                class="input-bordered input input-sm w-full"
                            />
                        </td>
                        <td class="p-4">
                            <input
                                bind:value={newContact.address}
                                id="address"
                                name="address"
                                type="text"
                                placeholder="Address"
                                class="input-bordered input input-sm w-full"
                            />
                        </td>
                        <td class="text-center p-4">
                            <button
                                on:click={() => contacts.add(newContact)}
                                id="addContactButton"
                                name="addContactButton"
                                type="submit"
                                class="btn-success btn-sm btn-square btn"
                            >
                                <UserPlusIcon size="16" />
                            </button>
                        </td>
                    </tr>
                    {#each $contacts as contact (contact.id)}
                        <tr class="bg-white hover:bg-gray-100 transition">
                            <th class="text-center">
                                <input
                                    on:click={() => contacts.favorite(contact.id)}
                                    id={`favoriteCheckbox${contact.id}`}
                                    name={`favoriteCheckbox${contact.id}`}
                                    type="checkbox"
                                    checked={contact.favorite}
                                    class="checkbox-accent checkbox checkbox-sm"
                                />
                            </th>
                            <td class="p-4">
                                <div class="flex items-center space-x-3">
                                    <div class="avatar">
                                        <div class="w-10 h-10 rounded-full overflow-hidden border border-gray-300">
                                            <img
                                                src={`https://id.lobstr.co/${contact.address}.png`}
                                                alt="Avatar"
                                                class="w-full h-full object-cover"
                                            />
                                        </div>
                                    </div>
                                    <div class="font-bold">{contact.name}</div>
                                </div>
                            </td>
                            <td class="p-4">
                                <TruncatedKey keyText={contact.address} lookupName={false} />
                            </td>
                            <td class="text-center p-4">
                                <button
                                    on:click={() => contacts.remove(contact.id)}
                                    id={`removeContact${contact.id}`}
                                    name={`removeContact${contact.id}`}
                                    class="btn-error btn-sm btn-square btn"
                                >
                                    <Trash2Icon size="16" />
                                </button>
                            </td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    </div>
</div>

<style>
    .input-bordered {
        border-radius: 0.5rem;
    }
</style>
