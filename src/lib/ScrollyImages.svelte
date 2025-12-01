<script>

	import "../assets/global-styles.css"	
	import { fade } from "svelte/transition";
	import { onMount, onDestroy } from "svelte";

	export let imageAlign = "center";
	export let imageWidth = "100%";
	export let imageHeight = "100%";
	export let textSectionAlign = "right";
	export let textSectionMaxWidth = "500px";
	export let fadeDuration = 250;
	export let sections = [
		{
		image: "/images/1.jpg",
		text: "<h2>Header</h2> <p>body text </p>",
		},
		{
		image: "/images/2.jpg",
		text: "<h2>Header</h2> <p>body text </p>",
		},
		{
		image: "/images/3.jpg",
		text: "<h2>Header</h2> <p>body text </p>",
		},
	];
	export let mobileTextAlign = "center";

	// $: topImageMargin = 0;

	// if ("%" or "dvh" or "vh" in imageHeight)

	// 	topImageMargin = (100 - imageHeight) / 2;

	// else ("px" in imageHeight)

		// imgDivHeight = min(0 ,(window.height - imageHeight) / 2)

	// $: topImageMargin = (100 - imageHeight) / 2;

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
				text: text
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
		let newIndex = currentIndex;
		textSections.forEach((section, index) => {
		const rect = section.getBoundingClientRect();
		if (
			rect.top <= window.innerHeight * 0.5 &&
			rect.bottom > window.innerHeight * 0.5
		) {
			newIndex = index;
		}
		});

		currentIndex = newIndex;
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
						transition:fade={{ duration: fadeDuration }}
						loading="lazy"
						style="max-height: {imageHeight}; max-width: {imageWidth}; top: {topImageMargin};"	
					/>
				</div>
				
			{/if}
			
		{/each}

		{#if isMobile}
			{#key currentIndex} 
				<div class="mobile-text-section mobile-text-{mobileTextAlign}"
						out:fade={{ duration: fadeDuration/2 }}
						in:fade={{  delay:fadeDuration/2, duration: fadeDuration/2 }}>
					<div class="mobile-text-wrapper" >
						{@html processedSections[currentIndex].text}
					</div>
				</div>
			{/key}
		{/if}
	</div>

	<div class="text-scroll">
		{#each processedSections as section, i}

			<div
				class="text-section {textSectionAlign}"
				bind:this={textSections[i]}
				style="max-width: {textSectionMaxWidth};"
			>

				<div class="text-wrapper {section.text.trim() ? '' : 'transparent'}">
					{@html section.text}
				</div>
			
			</div>

		{/each}
	</div>

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
		/* border: 1px solid #ccc; */
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

	.text-wrapper {
		padding-left: 20px;
		padding-right: 20px;
		position: relative;
		z-index: 1;
		background: rgba(255, 255, 255, 0.96);
		border: 1px solid #ccc;
	}

	.text-wrapper p {
		font-size: 25px;
	}

	.text-wrapper.transparent {
		background: transparent !important;
		border: none !important;
		opacity: 0;
		pointer-events: none;
		box-shadow: none;
	}

	.text-section.center {
		margin: 0 auto;
	}
	.text-section.right {
		margin: 0 0 0 auto;
	}
	.text-section.left {
		margin: 0 0 0 0;
		margin-left: 50px;
	}

	.text-section {
		padding: 30vh 2rem;
		position: relative;
		z-index: 1;
		text-align: left;
		height: 90vh;
	}

	@media (max-width: 500px) {
		.text-section { 
			padding: 30vh 0;
			width: 100%;
			max-width: 100vw !important;
			z-index: -10;
		}

		.text-section.left {
			margin-left: 0;
		}

		.image-container {
			z-index: 1;
		}

		.sticky-image img {
			position: absolute;
			object-fit: cover;
			object-position: 45% center;
			padding-top: 10vw;
			width: 96vw;
			height: 96vw; /* TODO: MAKE THIS CONFIGURABLE */
			margin: auto;
			border: 0;
			left: 0;
			right: 0;
			z-index: 1;
		}

		.text-wrapper {
			border: 0;
			opacity: 0;
		}

		.mobile-text-section {
			position: absolute;
			z-index: 5;
			margin-top: calc(96vw + 10vw);
    		width: 92vw;
			height: calc(100vh - 96vw - 10vw);
		}
		
		.mobile-text-top {
			display: flex;
			align-items: flex-start;   
			padding: 4vw 0 0 8vw;
			box-sizing: border-box;
		}

		.mobile-text-center {
			display: flex;
			align-items: center;   
			padding: 0 0 0 8vw;
			box-sizing: border-box;
		}

		.mobile-text-wrapper {
			display: inline-block;
			width: 100%; /* shrink-wrap the content */
		}

		:global(.mobile-text-wrapper p) {
			font-size: 16px !important;
			line-height: 28px;
		}
	}

	@media (max-width: 400px) {
		.sticky-image img {
			padding-top: 4vw;
		}

		.mobile-text-section {
			position: absolute;
			z-index: 5;
			margin-top: calc(96vw + 4vw);
    		width: 92vw;
			height: calc(100vh - 96vw - 4vw);
		}

		.mobile-text-top {
			display: flex;
			align-items: flex-start;   
			padding: 4vw 0 0 6vw;
			box-sizing: border-box;
		}

		.mobile-text-center {
			display: flex;
			align-items: center;   
			padding: 0 0 0 6vw;
			box-sizing: border-box;
		}

		:global(.mobile-text-wrapper p) {
			font-size: 15px !important;
			line-height: 24px;
		}
	}

</style>
