<script>

	import "../assets/global-styles.css"	
	import { fade } from "svelte/transition";
	import { onMount, onDestroy } from "svelte";
    import BottomArrow from "./BottomArrow.svelte";

	export let imageAlign = "center";
	export let imageWidth = "100%";
	export let imageHeight = "100%";
	export let textSectionAlign = "right";
	export let textSectionMaxWidth = "500px";
	export let fadeDuration = 250;
	export let sections = [
		{
		image: ["/images/1.jpg"],
		text: ["<h2>Header</h2> <p>body text </p>"],
		},
		{
		image: ["/images/2.jpg"],
		text: ["<h2>Header</h2> <p>body text </p>"],
		},
		{
		image: "/images/3.jpg",
		text: ["<h2>Header</h2> <p>body text </p>"],
		},
	];
	export let mobileTextAlign = "top";
	export let arrowColour = "white";

	$: console.log(imageHeight,windowHeight,topImageMargin);

	let windowHeight = 0;
	let imgDivHeight = 0;
	let topImageMargin = "0px";
	let isMobile = false;

	let processedSections = [];
	let numSections = 0;

	sections.forEach((item) => {
		item.text.forEach((text) => {
			processedSections.push({
				image: item.image,
				text: text,
				arrowColour: item.arrowColour ? item.arrowColour : "black"
			});
			numSections += 1;
		})
	})

	onMount(() => {
		windowHeight = window.innerHeight;
		isMobile = window.innerWidth <= 500;

		const resizeHandler = () => {
			windowHeight = window.innerHeight;
			isMobile = window.innerWidth <= 500;
		};
		window.addEventListener('resize', resizeHandler);

		return () => window.removeEventListener('resize', resizeHandler);
	});

	$: {
		if (typeof imageHeight === 'string') {
			if (imageHeight.includes('%') || imageHeight.includes('vh') || imageHeight.includes('dvh')) {
				const num = parseFloat(imageHeight);
				topImageMargin = `${(100 - num) / 2}dvh`;
			} else if (imageHeight.includes('px')) {
				const px = parseFloat(imageHeight);
				imgDivHeight = Math.max(0, (windowHeight - px) / 2);
				topImageMargin = `${imgDivHeight}px`;
			}
		}
	}

	
	let container;
	let currentIndex = 0;
	let textSections = [];

	const handleScroll = () => {
		currentIndex = Math.min(Math.floor(window.scrollY / windowHeight), processedSections.length - 1);
		arrowColour = processedSections[currentIndex].arrowColour;
	};


	onMount(() => {
		window.addEventListener("scroll", handleScroll);
		handleScroll();
		return () => {
			window.removeEventListener("scroll", handleScroll);
		};
	});

</script>



<div class="scrolly-wrapper" bind:this={container}>

	<div class="sticky-image">

		{#each processedSections as section, i}

			{#if currentIndex === i}
				<div class="image-container">
					<img
						class={imageAlign}
						src={section.image}
						alt={section.heading}
						transition:fade={section.image !== processedSections[currentIndex - 1]?.image
									? { duration: fadeDuration }
									: null}
						loading="eager"
						style="max-height: {imageHeight}; max-width: {imageWidth}; top: {topImageMargin};"	
					/>
				</div>
				
			{/if}
			
		{/each}

		{#key currentIndex} 
			<div class="fading-text-section fading-text-{mobileTextAlign}"
					out:fade={{ duration: fadeDuration/2 }}
					in:fade={{  delay:fadeDuration/2, duration: fadeDuration/2 }}>
				<div class="fading-text-wrapper" >
					{@html processedSections[currentIndex].text}
				</div>
			</div>
		{/key}
	</div>

	<div class="text-scroll" style:height="{windowHeight*processedSections.length}px"></div>

</div>



<style>
	
	.scrolly-wrapper {
		display: flex;
		flex-direction: column;
		position: relative;
		background-color: #f9f9f9;
		margin-top: 0px;
		margin-bottom: 50px;
	}

	.sticky-image {
		position: sticky;
		top: 0vh;
		height: 100dvh;
		width: 100%;
		z-index: 0;
	}

	.sticky-image img {
		position: absolute;
		object-fit: contain;
		height: 100%;
	}

	img.right {
		right: 0;
	}

	img.left {
		left: 0;
	}

	img.center {
		left: 50%;
		transform: translateX(-50%);
	}

	.fading-text-section {
		position: absolute;
		z-index: 5;
		width: 27vw;
		height: 100vh;
		display: flex;
		align-items: center;   
		padding: 0 0 0 2vw;
		box-sizing: border-box;
	}

	.fading-text-wrapper {
		display: inline-block;
		width: 100%; 
	}

	@media (max-width: 1450px) {
		.fading-text-section {
			position: absolute;
			z-index: 5;
			width: 23vw;
			height: 100vh;
			display: flex;
			align-items: center;   
			padding: 0 0 0 2vw;
			box-sizing: border-box;
		}

		:global(.fading-text-wrapper p) {
			font-size: 17px !important;
			line-height: 28px;
		}
	}

	@media (max-width: 1350px) {
		.sticky-image img {
			position: absolute;
			object-fit: cover;
			object-position: 35% center;
			width: 75vw;
			height: 96vh; 
			margin: auto;
			margin-left: 20vw;
			border: 0;
			left: 0;
			right: 0;
			z-index: 1;
		}
	}

	@media (max-width: 1100px) {
		.sticky-image img {
			position: absolute;
			object-fit: cover;
			object-position: 45% center;
			width: 75vw;
			height: 96vh; 
			margin: auto;
			margin-left: 23vw;
			border: 0;
			left: 0;
			right: 0;
			z-index: 1;
		}
	}

	@media (max-width: 850px) {
		.image-container {
			z-index: 1;
		}

		.sticky-image img {
			object-position: 45% center;
			padding-top: 2vw;
			width: 96vw;
			height: 96vw; /* TODO: MAKE THIS CONFIGURABLE */
			margin: auto;
		}
		
		.fading-text-section {
			position: absolute;
			z-index: 5;
			margin-top: calc(96vw + 2vw);
    		width: 94vw;
			height: calc(100vh - 96vw - 2vw);
		}
		
		.fading-text-top {
			display: flex;
			align-items: flex-start;   
			padding: 1vw 0 0 6vw;
			box-sizing: border-box;
		}

		:global(.fading-text-wrapper p) {
			font-size: 18px !important;
			line-height: 28px;
		}
	}

	@media (max-width: 500px) {
		.image-container {
			z-index: 1;
		}

		.sticky-image img {
			padding-top: 10vw;
		}
		
		.fading-text-section {
			margin-top: calc(96vw + 10vw);
    		width: 92vw;
			height: calc(100vh - 96vw - 10vw);
		}
		
		.fading-text-top {
			padding: 4vw 0 0 8vw;
		}

		:global(.fading-text-wrapper p) {
			font-size: 16px !important;
			line-height: 28px;
		}
	}

	@media (max-width: 400px) {
		.sticky-image img {
			padding-top: 4vw;
		}

		.fading-text-section {
			margin-top: calc(96vw + 4vw);
    		width: 92vw;
			height: calc(100vh - 96vw - 4vw);
		}

		.fading-text-top {
			padding: 4vw 0 0 6vw;
		}

		.fading-text-center {  
			padding: 0 0 0 6vw;
		}

		:global(.fading-text-wrapper p) {
			font-size: 15px !important;
			line-height: 24px;
		}
	}

</style>
