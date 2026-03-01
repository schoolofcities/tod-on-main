<script>

	import "../assets/global-styles.css"
	import LogoSofC from '../assets/sofc-uoft-logo-white.svg';
	import LogoII from '../assets/ii-logo-white.svg'

	import AuthorDate from "./AuthorDate.svelte";
	import { onMount } from "svelte";
    import TitleText from "./TitleText.svelte";

	// Text Props
	export let title = '';
	export let subtitle;
	export let type = '';
	export let location;
	export let titleFontColour = 'var(--brandDarkBlue)';
	export let subtitleFontColour = 'var(--brandDarkBlue)';
	export let logoType = 'White';
	export let secondLogo;

	let textProps = {
		title: title,
		subtitle: subtitle,
		type: type,
		location: location,
		titleFontColour: titleFontColour,
		subtitleFontColour: subtitleFontColour,
		logoType: logoType,
		secondLogo: secondLogo
	}
	
	export let bgType = 'Image'; // Image or Video 
	export let url; // background Image/Video url
	export let tintOpacity = 0;
	export let tintColour = "black";
	export let imageOpacity = 1;
	export let imageAltText = '';
	export let topOpacity = 1;
	export let videoOpacity = 1;
	export let videoSpeed = 1;      // <-- playback speed prop

	let divWidth;
	let videoEl;
	
	let isMobile = false;
	
	// reactively update playback speed
	$: if (videoEl) {
		videoEl.playbackRate = videoSpeed;
	}

	onMount(() => {
		isMobile = window.innerWidth <= 500;
		
		const resizeHandler = () => {
			isMobile = window.innerWidth <= 500;
		};
		window.addEventListener('resize', resizeHandler);

		return () => window.removeEventListener('resize', resizeHandler);
	})
</script>


<div class="title-container" class:video={bgType == "Video"} bind:clientWidth={divWidth} inert={topOpacity < 0.02}>

	<TitleText {...textProps}
	/>
	
	<div class="tint-overlay"
		style:opacity={tintOpacity}
		style:background={tintColour}></div>

	{#if bgType == "Image"}
		<div
			class="background-image"
			style="
				background-image: url({url});
				opacity: {imageOpacity};
				transition: background-position 1.5s ease-in;
			"
		></div>
	{:else if bgType == "Video"}
		<video
			class="background-video"
			bind:this={videoEl}
			autoplay
			muted
			loop
			playsinline
			style="opacity: {videoOpacity};"
		>
			<source src={url} type="video/mp4" />
		</video>
	{/if}

	
</div>


<style>

	.title-container {
		height: 100dvh;
		width: 100%;
		background-color: white;
		position: relative;
		margin-bottom: 0px;
		border-bottom: solid 3px white;
		display: flex;
		align-items: center;
	}

	.tint-overlay {
		position: fixed;
		width: 100%;
		height: 100%;
		z-index: 5;
	}

	.background-image {
		position: absolute;
		width: 100%;
		height: 100%;
		background-size: cover; 
		background-position: center;
		background-repeat: no-repeat;
	}

	.background-video {
		position: absolute;
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	@media (max-width: 600px) {
		.title-container.video {
			height: calc(100dvh - 250px);
			margin-bottom: 5px;
		}
	}

</style>