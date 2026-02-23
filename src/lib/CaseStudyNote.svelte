<script>
	// import '../assets/global-styles.css';

	export let style = 1;

</script>

<div class={`style-${style}`}>
	<p>
		The School of Cities has created five case studies of different kinds of transit-oriented development across Canada to explore the opportunities and trade-offs involved in creating thriving communities near transit. In each case, we explore current patterns of growth and project what that community might look like in 20-30 years if development continues in this way (the current trajectory). We then explore an alternative, “optimized” scenario that imagines policy and design changes that could address key challenges.
	</p>
</div>

<style>
	div {
		margin-top: 50px;
	}

	.style-1 {
		border-radius: 5px;
		border: 1px solid var(--brandGray70);
		padding: 20px;
		background-color: rgb(0, 0, 0, 0.1);
	}

	.style-1 p {
		padding: 0px;
		margin: 0px;
		font-style: italic;
	}

	.style-2 {
		border: 1px solid var(--brandGray70);
		box-shadow: 0px 0px 20px rgb(0, 0, 0, 0.38);
		padding: 20px;
	}

	.style-2 p {
		padding: 0px;
		margin: 0px;
	}

	.style-3 {
		border-radius: 25px;
		background-color: rgb(0, 0, 0, 0.1);
		padding: 30px;
	}

	.style-3 p {
		padding: 0px;
		margin: 0px;
		font-family: PoppinsRegular;
		font-size: 17px;
	}

</style>
