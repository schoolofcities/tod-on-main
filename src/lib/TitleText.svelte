<script>
	import "../assets/global-styles.css"
	import LogoBlack from '../assets/sofc-uoft-logo-black.svg';
	import LogoWhite from '../assets/sofc-uoft-logo-white.svg';
	import LogoII from '../assets/ii-logo-white.svg'

	export let title = '';
	export let subtitle;
	export let type = '';
	export let location;
	export let titleFontColour = 'var(--brandDarkBlue)';
	export let subtitleFontColour = 'var(--brandDarkBlue)';
	export let logoType = 'White';
	export let secondLogo;
	let divWidth;

	let Logo;
	$: Logo = logoType === 'Black'
		? LogoBlack
		: logoType === 'White'
		? LogoWhite
		: '';
</script>


<div class="title-container {type.replace(" ","-").toLowerCase()}" bind:clientWidth={divWidth}>
	<div class="upper-section">
		<div class="logo-container">
			{#if logoType !== 'None'}
				<a href="https://schoolofcities.utoronto.ca/" target="_blank" class="logo-link">
					<img src={Logo} alt="UofT and School of Cities logos" class="logo-top" />
				</a>
			{/if}
			{#if secondLogo == "II"}
				<a href="https://infrastructureinstitute.ca/" target="_blank" class="logo-link">
					<img src={LogoII} alt="Infrastructure Institute logo" class="logo-top" id="ii-logo"/>
				</a>
			{/if}
		</div>

		<h3 class="type-text" style="color: {titleFontColour};">
			{type.toUpperCase()}
		</h3>
	</div>

	<div class="main-title" class:no-subtitle={typeof subtitle == 'undefined'}>
		<div>
			<h1 class="title-text" style="color: {titleFontColour};">
				{type.toLowerCase() == "research" ? title : title.toUpperCase()}
			</h1>
			{#if location}
				<h3 class="location-text" style="color: {titleFontColour}">
					{location.toUpperCase()}
				</h3>
			{/if}
		</div>
	</div>

	{#if subtitle}
		<div class="lower-section">
			<h2 class="subtitle-text" style="color: {subtitleFontColour};">
				{subtitle}
			</h2>
		</div>
	{/if}

</div>



<style>
	.title-container {
		height: 100%;
		width: 100%;
		position: relative;
		padding-left: 20rem;
		z-index: 10;
	}

	.upper-section {
		position: absolute;
		top: 24rem;
		height: 27%;
		width: 100%;
	}

	.logo-container {
		position: absolute;
		z-index: 2;
	}

	.logo-link {
		filter: drop-shadow(0px 0px 20px rgba(0, 0, 0, 2))
	}

	.logo-link:hover {
		opacity: 0.8;
	}

	.type-text {
		position: absolute;
		bottom: 0;
		font-family: PoppinsSemiBold;
		font-weight: normal;
		font-size: 8rem;
		text-shadow: 0px 0px 10px rgba(0, 0, 0, 2); 
	}

	.main-title {
		position: absolute;
		top: calc(27% + 24rem);
		bottom: 23%;
		width: 100%;
		display: flex;
		align-items: center;
	}

	.title-text {
		max-width: 800px;
		width: 75%;
		left: 20rem;
		font-family: PoppinsBold;
		font-weight: normal;
		margin-left: -1rem;
		margin-top: 0;
		text-shadow: 0px 0px 20px rgba(0, 0, 0, 0.6); 
		letter-spacing: -0.75rem;
	}

	.case-study .title-text {
		font-size: 64px;
		line-height: 60px;
	}

	.research .title-text {
		font-size: 50px;
		line-height: 60px;
	}

	.location-text {
		font-size: 6rem;
		text-shadow: 0px 0px 10px rgba(0, 0, 0, 2); 
	}

	.lower-section {
		position: absolute;
		bottom: 0;
		height: 23%;
		width: 100%;
	}

	.subtitle-text {
		position: absolute;
		margin-top: 0;
		max-width: 600px;
		font-size: 8rem;
		font-family: PoppinsMedium;
		font-weight: normal;
		text-shadow: 0px 0px 20px rgba(0, 0, 0, 0.6); 
	}

	@media (max-width: 600px) {
		.title-container {
			width: 100dvw;
			padding-left: 30px;
			margin-right: 30px;
		}

		.logo-container {
			width: 80%;
			display: flex;
			flex-wrap: wrap;
		}

		.upper-section {
			top: 30px;
			height: 30%;
		}

		.lower-section {
			height: 25%;
		}

		.main-title {
			top: calc(30% + 30px);
			width: 100%;
		}

		.main-title.no-subtitle {
			bottom: 0;
		}

		.title-text {
			width: calc(100% - 30px - 30px);
		}
		
		.case-study .title-text {
			font-size: 54px;
			line-height: 50px;

		}

		.research .title-text {
			font-size: 35px;
			line-height: 40px;
		}

		.main-title.no-subtitle .title-text{
			font-size: 40px;
			line-height: 50px;
		}

		.subtitle-text {
			width: calc(100% - 30px);
		}

		.research .subtitle-text, .research .type-text {
			font-size: 18px;
		}

	}

</style>
