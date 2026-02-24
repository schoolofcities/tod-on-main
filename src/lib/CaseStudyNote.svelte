<script>
	// import '../assets/global-styles.css';

	export let style = 1;

</script>

<div class={`style-${style}`}>
	<p>
		This is one of five case studies produced by the <a href="https://schoolofcities.utoronto.ca/" target="_blank">School of Cities</a> to identify different kinds of transit-oriented development across Canada and to explore the opportunities and trade-offs involved in creating thriving communities near transit. In each case, we examine current patterns of growth and project what that community might look like in 20-30 years if development continues in this way (the “current trajectory”). We then present an alternative, “optimized” scenario that imagines policy and design changes that could address common challenges. All station area renderings are conceptual and should not be interpreted as specific guidance for individual properties. Renderings were created by the <a href="https://infrastructureinstitute.ca/" target="_blank">Infrastructure Institute</a> in 2025 and may not reflect more recent proposals. 
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
		background-color: rgb(0, 0, 0, 0.05);
	}

	.style-1 p {
		padding: 0px;
		margin: 0px;
		font-style: italic;
		font-family: PoppinsItalic;
	}

	.style-2 {
		border: 1px solid var(--brandGray70);
		box-shadow: 0px 0px 20px rgb(0, 0, 0, 0.38);
		padding: 20px;
	}

	.style-2 p {
		font-family: PoppinsRegular;
		padding: 0px;
		margin: 0px;
	}

	.style-3 {
		border-radius: 25px;
		background-color: rgb(0, 0, 0, 0.03);
		padding: 30px;
	}

	.style-3 p {
		padding: 0px;
		margin: 0px;
		font-family: PoppinsRegular;
		line-height: 28px;;
		font-size: 16px;
	}

	.style-3 p a {
		font-family: inherit;
	}

</style>
