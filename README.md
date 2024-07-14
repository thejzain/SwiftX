**# SwiftX**

> A sample payments application built on Stellar's Testnet that facilitates international money transfers with currency conversion.

**Important Note:** SwiftX is for educational purposes only and shouldn't be used on Stellar's Mainnet.

**Key Functionality**

SwiftX allows users to send and receive payments internationally by:

* Converting local currency to Stellar Lumens (XML) for transfers across borders.
* Converting XML back to the recipient's local currency upon receiving the payment.

**Getting Started**

1. Clone the repository:

```bash
git clone https://github.com/your-username/swiftX.git
```

2. Install dependencies and start the development server:

```bash
cd swiftX
yarn install
yarn dev
```

3. Visit http://localhost:5173 in your browser.

**Exploring the Codebase**

This project uses Stellar's Testnet to showcase various Stellar features and SEPs (Stellar Ecosystem Proposals). Key areas to explore include:

* **Currency Conversion Logic:** Likely implemented in a dedicated component or service responsible for calculating exchange rates and converting between local currencies and XML.
* **Stellar Interactions:** Implemented using SEPs (code located in `/src/lib/stellar/sep*.js`). These interactions likely involve path payments to facilitate currency conversion on the Stellar network.
* **Stellar Network Queries:** Handled by `/src/lib/stellar/horizonQueries.js` to retrieve exchange rate data or other relevant information from the network.

**Additional Information**

This project builds upon the concepts demonstrated in the BasicPay application.
