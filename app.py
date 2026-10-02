import streamlit as st

st.set_page_config(
    page_title="Smart Vending Machine",
    page_icon="🪙"
)

st.title("🪙 Smart Vending Machine")
st.subheader("Minimum Coin Change using Dynamic Programming")

st.write(
    "This application finds the minimum number of coins "
    "required to return the exact change."
)

st.divider()

st.header("⚙️ Change Calculator")

coins_input = st.text_input(
    "Enter coin denominations",
    "1, 2, 5, 10"
)

amount = st.number_input(
    "Enter change amount",
    min_value=0,
    value=18,
    step=1
)

if st.button("🔍 Calculate Minimum Coins"):

    try:
        coins = [
            int(x.strip())
            for x in coins_input.split(",")
            if x.strip()
        ]

        if not coins:
            st.error("Please enter at least one coin.")

        elif any(coin <= 0 for coin in coins):
            st.error("Coin values must be greater than 0.")

        else:

            # Dynamic Programming
            dp = [float("inf")] * (amount + 1)

            selected_coin = [-1] * (amount + 1)

            dp[0] = 0

            for current in range(1, amount + 1):

                for coin in coins:

                    if coin <= current:

                        if dp[current - coin] + 1 < dp[current]:

                            dp[current] = dp[current - coin] + 1

                            selected_coin[current] = coin

            # Check whether solution exists
            if dp[amount] == float("inf"):

                st.error(
                    "❌ Change cannot be made "
                    "using the given coins."
                )

            else:

                # Find coins used
                combination = []

                current = amount

                while current > 0:

                    coin = selected_coin[current]

                    if coin == -1:
                        break

                    combination.append(coin)

                    current -= coin

                st.success(
                    f"✅ Minimum number of coins: {dp[amount]}"
                )

                st.info(
                    "🪙 Coins returned: "
                    + " + ".join(map(str, combination))
                )

                st.write(
                    f"**Total:** "
                    f"{' + '.join(map(str, combination))} = {amount}"
                )

    except ValueError:
        st.error(
            "❌ Please enter valid numbers separated by commas."
        )


st.divider()

st.header("🧠 Algorithm")

st.write(
    "We use Dynamic Programming to calculate the minimum "
    "number of coins for every amount from 0 to the required amount."
)

col1, col2 = st.columns(2)

with col1:
    st.metric("Time Complexity", "O(A × N)")

with col2:
    st.metric("Space Complexity", "O(A)")

st.divider()

st.caption("DAA Hackathon • Minimum Coin Change")