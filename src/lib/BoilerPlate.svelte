
<script>
    import AuthorDate from "./AuthorDate.svelte";


	export let pageType = "CaseStudy" // Research

	let boilerPlate = '';

	if (pageType === "CaseStudy") {
		boilerPlate = 'This is one of five case studies produced by the <a href="https://schoolofcities.utoronto.ca/" target="_blank">School of Cities</a> to identify different kinds of transit-oriented development across Canada and to explore the opportunities and trade-offs involved in creating thriving communities near transit. In each case, we examine current patterns of growth and project what that community might look like in 20-30 years if development continues in this way (the “current trajectory”). We then present an alternative, “optimized” scenario that imagines policy and design changes that could address common challenges. All station area renderings are conceptual and should not be interpreted as specific guidance for individual properties. Renderings were created by the <a href="https://infrastructureinstitute.ca/" target="_blank">Infrastructure Institute</a> in 2025 and may not reflect more recent proposals. <br><br>This work is part of the <a href="https://housing-infrastructure.canada.ca/rki-irc/index-eng.html" target="_blank">Research Knowledge Initiative</a> program from <a href="https://housing-infrastructure.canada.ca/index-eng.html" target="_blank">Housing, Infrastructure and Communities Canada</a> and developed in partnership with the <a href="https://canurb.org/" target="_blank">Canadian Urban Institute</a>.';
	} else if (pageType === "Research") {
		boilerPlate = 'This research brief is one of six produced by the <a href="https://schoolofcities.utoronto.ca/" target="_blank">School of Cities</a> to understand the benefits and trade-offs of building density near transit. Using case studies and data from across Canada, each brief examines how different forms of transit-oriented development (TOD) affect a core urban issue, such as municipal finances, displacement, equity, or greenhouse gas emissions. <br><br>This work is part of the <a href="https://housing-infrastructure.canada.ca/rki-irc/index-eng.html" target="_blank">Research Knowledge Initiative</a> program from <a href="https://housing-infrastructure.canada.ca/index-eng.html" target="_blank">Housing, Infrastructure and Communities Canada</a> and developed in partnership with the <a href="https://canurb.org/" target="_blank">Canadian Urban Institute</a>.';
	} else {
		boilerPlate = "meow";
	}

</script>




<div>
	<p>
		{@html boilerPlate}
	</p>
</div>




<style>
	div {
		margin-top: 50px;
		border-radius: 25px;
		background-color: rgb(0, 0, 0, 0.03);
		padding: 30px;
	}

	p {
		padding: 0px;
		margin: 0px;
		font-family: PoppinsRegular;
		line-height: 27px;;
		font-size: 16px;
	}

	p :global(a) {
        font-family: inherit;
    }

	@media (max-width: 500px) {
		div {
			padding: 20px;
		}
		p {
			font-size: 12px;
			line-height: 21px;
		}
	}

</style>
