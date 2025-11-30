<script>

	import "../assets/global-styles.css"
	import LogoSofC from '../assets/sofc-uoft-logo-white.svg';
	import LogoII from '../assets/ii-logo-white.svg'

	import AuthorDate from "./AuthorDate.svelte";
	import { onMount } from "svelte";

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
	export let authorText = "";
	export let dateText = "";
	export let topOpacity = 1;

	let divWidth;
	
	let isMobile = false;

	onMount(() => {
		isMobile = window.innerWidth <= 500;
		
		const resizeHandler = () => {
			isMobile = window.innerWidth <= 500;
		};
		window.addEventListener('resize', resizeHandler);

		return () => window.removeEventListener('resize', resizeHandler);
	})
</script>


<div class="title-container" bind:clientWidth={divWidth} >

	<div
        class="background-image"
		class:background-image-shifted={topOpacity < 0.6 && !isMobile}
        style="
            background-image: url({image});
            opacity: {imageOpacity};
			transition: background-position 1.5s ease-in;
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

		<!-- <img src={imageFeature} style="max-width: 90px; opacity: 1; border: solid 5px white; margin-bottom: -25px;"/> -->
		
		<h1 style="color: {titleFontColour};">{title}</h1>

		<!-- {#if divWidth > 600} -->

		<h2 style="color: {subtitleFontColour}; margin-bottom: 100px;">{subtitle}</h2>

		<!-- {/if} -->
		

		<div class="author-date">

			<p>
				{@html authorText}
				<br>
				<span id="date">{dateText}</span>
			</p>

		</div>

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

	.background-image-shifted {
		background-size: contain; 
		background-position: right;
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
		max-width: 1080px;
		position: absolute;
		bottom: 100px;
		left: 100px;
	}

	.title-text-container h1 {
		font-family: TradeGothicBold;
		font-weight: normal;
		font-size: 86px;
		text-decoration: none;
		margin-bottom: 10px;
		padding: 0px;
		text-shadow: 0px 0px 20px rgba(0, 0, 0, 0.6); 
	}

	.title-text-container h2 {
		max-width: 720px;
		text-align: left;
		font-family: SourceSerifBoldItalic;
		font-weight: normal;
		font-size: 32px;
		margin-top: 0px;
		text-shadow: 0px 0px 10px rgba(0, 0, 0, 2); 
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

	@media (max-width: 1000px) {
		.title-text-container h1 {
			font-size: 7vw;
		}
		.title-text-container h2 {
			font-size: 3vw;
		}
	}

	@media (max-width: 600px) {
		.title-container {
			/* height: calc(100dvh - 150px); */
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
	}

	.author-date {
		margin-top: 0px;
		padding-bottom: 0px;
		border-bottom: solid 1px var(--brandGray);
		margin-bottom: 25px;
	}

	.author-date p {
		font-size: 16px;
		line-height: 24px;
		color: var(--brandWhite);
	}

	.author-date a {
		color: white;
		text-decoration: none;
	}

	.author-date b {
		color: var(--brandGray80);
		font-family: SourceSerifBold;
		font-weight: normal;
	}

	.author-date strong {
		color: var(--brandGray80);
		font-family: SourceSerifBold;
		font-weight: normal;
	}

	.author-date #date {
		font-family: SourceSerifBold;
		font-size: 13px;
		font-weight: normal;
	}

</style>