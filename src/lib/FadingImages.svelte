<script>

	import "../assets/global-styles.css"	
	import { fade } from "svelte/transition";
	import { onMount, onDestroy } from "svelte";
    import { marked } from 'marked'
    import ScrollAnimate from '$lib/ScrollAnimate.svelte';

	export let imageAlign = "center";
	export let header = "";
	export let imageWidth = "100%";
	export let imageHeight = "100%";
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
	export let mobileTextAlign = "top";
	export let arrowColour = "white";
	export let backgroundColour = "#FAFAFA";

	let windowHeight = 0;
	let imgDivHeight = 0;
	let topImageMargin = "0px";
	let isMobile = false;
	let numSections = sections.length;
	let mounted = false;
	let showAnimation;


	onMount(() => {
		windowHeight = window.innerHeight;
		isMobile = window.innerWidth <= 550 && window.innerWidth / window.innerHeight <= 0.8;
		mounted = true;

		const resizeHandler = () => {
			windowHeight = window.innerHeight;
			hideDownArrow = isMobile && hideDownArrow;
			hideUpArrow = isMobile && hideUpArrow;
			isMobile = window.innerWidth <= 550 && window.innerWidth / window.innerHeight <= 0.8;
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

	$: if (mounted) {
		const preloadCount = 2;
		for (let i = 1; i <= preloadCount; i++) {
			const next = sections[currentIndex + i];
			if (!next) continue;

			if (next.image.valueOf() != sections[currentIndex].image.valueOf()){
				const img = new Image();
				img.src = next.image;
			}

			if (next.overlay1) {
				const o1 = new Image();
				o1.src = next.overlay1;
			}
			if (next.overlay2) {
				const o2 = new Image();
				o2.src = next.overlay2;
			}
		}
	}
	let containerTop = 0;
	let containerHeight = 0;
	let hideProgressBar = true;

	const measureContainer = () => {
		const rect = container.getBoundingClientRect();
		containerTop = rect.top + window.scrollY;
		containerHeight = rect.height;
	};

	const handleScroll = () => {
		const scrollY = window.scrollY;
		const localScroll = scrollY - containerTop;
		const sectionHeight = windowHeight;

		if (localScroll < 0 || localScroll > containerHeight - sectionHeight) {
			hideProgressBar = true;
			return;
		}
		
		const index = Math.floor(localScroll / sectionHeight);

		hideProgressBar = index < 0 || index >= numSections;

		currentIndex = Math.min(
			Math.max(index, 0),
			numSections - 1
		);


		arrowColour = sections[currentIndex].arrowColour;
	};


	onMount(() => {
		window.addEventListener("scroll", handleScroll);
  		window.addEventListener("resize", measureContainer);
		handleScroll();
  		measureContainer();
		return () => {
			window.removeEventListener("scroll", handleScroll)
			window.removeEventListener("resize", measureContainer);
		};
	});

</script>



<div class="scrolly-wrapper" bind:this={container} style:background-color={backgroundColour}>
	<ScrollAnimate 
		colour={arrowColour}></ScrollAnimate>

	<div class="tracker" style:display={hideProgressBar ? "none" : "flex"}>
		{#each sections as section, i}
			{#if section.bg_fit == "contain"}
				<div class="segment">
					<div
						class="fill"
						style="width:{currentIndex >= i ? "100%": "0%"}">
					</div>
				</div>
			{/if}
		{/each}
	</div>

	<div class="sticky-image">
		{#key currentIndex} 
			<div class="image-container">
				<img
					class={`${imageAlign} ${sections[currentIndex].bg_fit}`}
					src={sections[currentIndex].image}
					alt={sections[currentIndex].heading}
					transition:fade={{duration: sections[currentIndex].image.valueOf() != sections[currentIndex - 1]?.image.valueOf()
								? fadeDuration : 0 }}
					loading="eager"
					style="max-height: {imageHeight}; max-width: {imageWidth}; top: {topImageMargin};"	
				/>
			</div>
		{/key}
		
		{#if header != ""}
			<h1 class="header-text"
				style="color: {arrowColour}">
				{header}
			</h1>
		{/if}

		{#key currentIndex} 
			<div class="fading-text-section fading-text-{mobileTextAlign}"
					out:fade={{ duration: sections[currentIndex].text.valueOf() != sections[currentIndex - 1]?.text.valueOf() ? fadeDuration/2 : 0 }}
					in:fade={{  delay: sections[currentIndex].text.valueOf() != sections[currentIndex - 1]?.text.valueOf() ? fadeDuration/2 : 0, 
								duration: sections[currentIndex].text.valueOf() != sections[currentIndex - 1]?.text.valueOf() ? fadeDuration/2 : 0}}>
				<div class="fading-text-wrapper" >
					{@html marked(sections[currentIndex].text)}
				</div>
			</div>
		{/key}

		<div class="fading-overlay-section">
			<div class="desktop-overlay"
				style="visibility: {isMobile ? "hidden" : "visible"}">
			
				{#if sections[currentIndex].overlay1 != ""}
					<div class="overlay-1 overlay-image" >
						<img
						src={sections[currentIndex].overlay1}
						alt={sections[currentIndex].overlay1}
						transition:fade={{duration: sections[currentIndex].overlay1.valueOf() != sections[currentIndex - 1]?.overlay1.valueOf()
									? fadeDuration : 0 }}
						/>
					</div>
				{/if}

				{#if sections[currentIndex].overlay2 != ""}
					<div class="overlay-2 overlay-image" >
						<img
						src={sections[currentIndex].overlay2}
						alt={sections[currentIndex].overlay1}
						transition:fade={{duration: sections[currentIndex].overlay2.valueOf() != sections[currentIndex - 1]?.overlay2.valueOf()
									? fadeDuration : 0 }}
						/>
					</div>
				{/if}
			</div>
		</div>
	</div>

	<div class="mobile-overlay text-scroll"
		style="visibility: {isMobile ? "visible" : "hidden"}">
			{#each sections as section, i}
				<div id={section.menu_id !== "" ? section.menu_id : null}>
					{#if section.overlay2 == ""}
						<div class="mobile-overlay-1 mobile-overlay-image">
							<img
							src={section.overlay1}
							alt={section.overlay1}
							/>
						</div>
					{/if}
					{#if section.overlay2 !== ""}
						<div class="mobile-overlay-2 mobile-overlay-image">
							<img
							src={section.overlay2}
							alt={section.overlay2}
							/>
						</div>
					{/if}
				</div>
			{/each}
	</div>


</div>



<style>
	.tracker {
		position: fixed;
		gap: 4rem;
		right: 50%;
		transform: translateX(20%);
		bottom: 20rem;
		z-index: 20;
		width: fit-content;
		height: fit-content;
	}
	
	.segment {
		flex: 1;
		background: rgba(145, 145, 145, 0.26);
		overflow: hidden;
		border-radius: 100px;
		height: 1.5rem;
		width: 10rem;
	}

	.fill {
		height: 100%;
		background: rgb(100, 100, 100);
		width: 0%;
		transition: width 0.1s linear;
		border-radius: 100px;
	}
	
	.scrolly-wrapper {
		display: flex;
		flex-direction: column;
		position: relative;
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
		height: 100%;
	}

	.sticky-image img.cover {
		width: 100%;
		object-fit: cover; 
		background-position: center;
		background-repeat: no-repeat;
	}

	.sticky-image img.contain {
		object-fit: contain;
	}

	.header-text {
		position: absolute;
		top: 15rem;
		left: 15rem;
		width: 18rem;
		font-size: 8rem;
		line-height: 6.5rem;
		letter-spacing: -0.30rem;
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
		width: 25vw;
		height: 100vh;
		display: flex;
		align-items: center;   
		padding: 0 0 0 15rem;
		box-sizing: border-box;
	}

	.fading-text-wrapper {
		display: inline-block;
		width: 100%; 
	}

	.fading-overlay-section {
		position: absolute;
		z-index: 5;
		width: 25vw;
		height: 100vh;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		gap: 3rem;
		right: 15rem;
		box-sizing: border-box;
	}

	.fading-overlay-section img {
		position: relative;
		object-fit: contain;
		width: 100%;
	}

	.mobile-overlay-image {
		height: 100vh;
		width: 100%;
	}

	.mobile-overlay-image img {
		width: 100%;
		box-shadow: 0px 0px 2px black;
	}

	.mobile-overlay {
		width: 96vw;
		left: 2vw;
		position: relative;
	}

	#slide-count {
		z-index: 10;
		right: 15rem;
		bottom: 15rem;
        position: fixed;
	}

	@media (max-width: 1450px) {
		.fading-text-section {
			position: absolute;
			z-index: 5;
			width: 23vw;
			height: 100vh;
			display: flex;
			align-items: center;   
			padding: 0 0 0 10rem;
			box-sizing: border-box;
		}

		:global(.fading-text-wrapper p) {
			font-size: 17px !important;
			line-height: 28px;
		}

		.header-text {
			position: absolute;
			top: 10rem;
			left: 10rem;
		}
	}

	@media (max-aspect-ratio: 5/6) {
		.image-container {
			z-index: 1;
		}

		.sticky-image img {
			object-fit: cover;
		}

		.sticky-image img.contain {
			object-fit: contain;
			object-position: 45% center;
			padding-top: 2vw;
			width: 96vw;
			height: 96vw; 
			margin: auto;
		}
		
		.fading-text-section {
			position: absolute;
			z-index: 5;
			margin-top: calc(94vw);
    		width: 94vw;
			height: calc(100vh - 94vw);
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

		.header-text {
			font-size: 7rem;
		}
	}

	@media (max-width: 650px) and (max-aspect-ratio: 5/6) {
		:global(.fading-text-wrapper p) {
			margin-top: -15vw;
		}
	}

	@media (max-width: 500px) {
		.image-container {
			z-index: 1;
		}

		.sticky-image img {
			object-fit: cover;
		}

		.sticky-image img.contain {
			padding-top: 10vw;
		}
		.fading-text-section {
    		width: 92vw;
			height: calc(100vh - 96vw - 10vw);
		}
		
		.fading-text-top {
			padding: 4vw 0 0 8vw;
		}

		:global(.fading-text-wrapper p) {
			font-size: 16px !important;
			line-height: 28px;
			margin-top: 0;
		}
	}

	@media (max-width: 400px) {

		.fading-text-section {
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
