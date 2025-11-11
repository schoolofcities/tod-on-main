<script>

	import "../assets/global-styles.css"
	import LogoSofC from '../assets/sofc-uoft-logo-blue-colour.svg';
	import LogoII from '../assets/ii-logo.svg'

	import AuthorDate from "./AuthorDate.svelte";

	export let title = '';
	export let subtitle = '';
	export let image = '';
	export let imageOpacity = 1;
	export let imageAltText = '';
	// export let imageCaption = '';
	// export let imageSource = '';
	export let imageFeature = '';
	export let titleFontColour = 'var(--brandDarkBlue)';
	export let subtitleFontColour = 'var(--brandDarkBlue)';
	export let logoType = 'Black'; // 'Black', 'White', or 'None'

	let divWidth;

</script>


<div class="title-container" bind:clientWidth={divWidth} >

	<div
        class="background-image"
        style="
            background-image: url({image});
            opacity: {imageOpacity};
        "
    ></div>

	<div class="logo-container">

		{#if logoType !== 'None'}
			<a href="https://schoolofcities.utoronto.ca/" target="_blank" class="logo-link">
				<img src={LogoSofC} alt="UofT and School of Cities logos" class="logo-top" />
			</a>
			<a href="https://infrastructureinstitute.ca/" target="_blank" class="logo-link">
				<img src={LogoII} alt="Infrastructure Institute logo" class="logo-top" />
			</a>
		{/if}
		
	</div>

	<div class="title-text-container">

		<img src={imageFeature} style="max-width: 90px; opacity: 1; border: solid 5px white; margin-bottom: -25px;"/>
		
		<h1 style="color: {titleFontColour};">{title}</h1>

		<!-- {#if divWidth > 600} -->

		<h2 style="color: {subtitleFontColour}; margin-bottom: 100px;">{subtitle}</h2>

		<!-- {/if} -->
		

		<AuthorDate
			authors="<a href='' target='_blank'>Author Name</a>, <a href='' target='_blank'>Author Name</a></a>, & <a href='' target='_blank'>Author Name</a>"
			date="December 2025"
		/>

	</div>

</div>

<!-- <div class="subtitle-text-container">
		
	{#if divWidth <= 600}

		<h2 style="color: black;">{subtitle}</h2>
		
	{/if}

</div> -->



<style>

	.title-container {
		height: 100dvh;
		width: 100%;
		background-color: white;
		position: relative;
		margin-bottom: 0px;
		border-bottom: solid 3px white;
		
	}

	.background-image {
		position: absolute;
		width: 100%;
		height: 100%;
		background-size: cover; 
		background-position: center; 
		background-repeat: no-repeat;
	}

	.logo-container {
		position: absolute;
		top: 100px;
		left: 100px;
	}

	.logo-container:hover {
		opacity: 0.8;
	}

	.title-text-container {
		max-width: 720px;
		position: absolute;
		bottom: 100px;
		left: 100px;
	}

	.title-text-container h1 {
		font-family: TradeGothicBold;
		font-weight: normal;
		font-size: 60px;
		text-decoration: none;
		margin-bottom: 10px;
		padding: 0px;
		/* text-shadow: 0px 0px 20px rgba(0, 0, 0, 0.6);  */
	}

	.title-text-container h2 {
		text-align: left;
		font-family: SourceSerifBoldItalic;
		font-weight: normal;
		font-size: 25px;
		margin-top: 0px;
		/* text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.8);  */
	}

	.subtitle-text-container {
		max-width: 600px;
		margin: 20px;
	}

	.subtitle-text-container h2 {
		font-size: 22px;
		font-family: SourceSerifItalic;
		font-weight: normal;
	}

	/* @media (max-width: 600px) {
		.title-container {
			height: calc(100dvh - 150px);
			margin-bottom: 5px;
		}
		.logo-container {
			left: 20px;
			top: 10px;
		}
		.title-text-container {
			left: 20px;
			bottom: 10px;
			padding-right: 10px;
		}
		.title-text-container h1 {
			font-size: 48px;
		}
		.title-text-container h2 {
			font-size: 24px;
		}
	} */

</style>