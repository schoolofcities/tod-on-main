<script>

	import "../assets/global-styles.css"	
	import { fade } from "svelte/transition";
	import { onMount, onDestroy } from "svelte";
    import { marked } from 'marked';

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

	<div class="tracker" style:display={hideProgressBar ? "none" : "flex"}>
		{#each sections as section, i}
			{#if section.bg_fit == "contain" && i != 0}
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
			<div class="fading-text-section fading-text-{mobileTextAlign} {isMobile ? "" : imageAlign}"
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
	/* progress bar */
	.tracker {
		position: fixed;
		gap: 4rem;
		right: 50%;
		transform: translateX(50%);
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
	

	/* scrolly setup */
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
		left: 50%;
		transform: translateX(-50%);
	}

	.sticky-image img.contain {
		object-fit: contain;
		max-width: 70vw;
	}

	.header-text {
		position: absolute;
		left: 15rem;
		width: 18rem;
		font-size: 8rem;
		line-height: 6.5rem;
		letter-spacing: -0.30rem;
		margin-top: 15rem !important;
	}

	img.right {
		right: 7vw;
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

	@media (min-aspect-ratio: 7/4) {
		.fading-text-section.right {
			left: 7vw;
			width: 30vw;
		}

		img.right {
			right: 7vw;
		}
		
		.fading-text-section.center {
			width: 25vw;
		}
	}
	
	@media (min-aspect-ratio: 6/5) {

		:global(.fading-text-wrapper p) {
			font-size: 17px !important;
			line-height: 28px;
		}
		
		.fading-text-section.center {
			width: 20vw;
		}

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

		.header-text {
			position: absolute;
			margin-top: 15rem !important;
			left: 10rem;
		}

		:global(.fading-text-wrapper p) {
			font-size: max(6rem, 14.5px) !important;
			line-height: 28px;
			margin-top: 0;
		}
	}


	@media (max-aspect-ratio: 6/5) {
		.fading-text-section.right {
			width: 94vw;
		}

		img.right {
			right: 2vw;
		}

		.fading-text-section {
			position: absolute;
			z-index: 5;
			margin-top: calc(67vw);
    		width: 94vw;
			height: calc(100vh - 94vw);
			max-width: 680px;
			left: 50%;
			transform: translateX(-50%);
			padding: 0;
		}

		img {
			left: 50%;
			transform: translateX(-50%);
		}

		.image-container {
			z-index: 1;
			width: fit-content;
		}

		.sticky-image img {
			object-fit: cover;
		}

		.sticky-image img.contain {
			object-fit: contain;
			object-position: 45% center;
			width: 96vw;
			height: 96vw; 
			margin-top: -10vw;
		}
		
		.fading-text-top {
			display: flex;
			align-items: flex-start;   
			box-sizing: border-box;
		}

		:global(.fading-text-wrapper p) {
			font-size: min(4.75rem, 16px) !important;
			line-height: 28px;
		}

		.header-text {
			font-size: 7rem;
		}
	}

	@media (max-aspect-ratio: 1) {
		.sticky-image img.contain.center {
			top: -5vh;
		}

		.sticky-image img.contain.right {
			top: -5vh;
		}
		.fading-text-section {
			position: absolute;
			z-index: 5;
			margin-top: calc(70vw + 5vh);
    		width: 94vw;
			height: calc(100vh - 94vw);
			max-width: 680px;
			left: 50%;
			transform: translateX(-50%);
			padding: 0;
		}


		.sticky-image img.contain {
			object-fit: contain;
			object-position: 45% center;
			margin-top: 5vw;
			width: 96vw;
			height: 96vw; 
			margin: auto;
		}
	}

	@media (max-aspect-ratio: 5/6) {
		.fading-text-wrapper {
			margin-top: -10vw;
		}

		.fading-text-section {
			margin-top: calc(97vw);
		}

		.sticky-image img.cover {
			max-width: 100vw;
		}
		.sticky-image img.contain {
			max-width: 100vw;
			padding-top: 5vh;
    		width: 92vw;
		}

		.fading-text-section.right {
			width: 94vw;
		}
		
		.sticky-image img.contain.center {
			top: 0vh;
		}
		.sticky-image img.contain.right {
			top: 0vh;
		}
	}

	/* @media (max-width: 675px) { */
	@media (max-aspect-ratio: 4/5) {
		.sticky-image img.contain {
			padding-top: 5vw;
		}

		.fading-text-section {
    		width: 92vw;
			height: calc(100vh - 96vw - 30vw);
			margin-top: calc(100vw);
		}

		:global(.fading-text-wrapper p) {
			font-size: max(4.75rem, 14px) !important;
			line-height: 28px;
			margin-top: 0;
		}
	}

	/* @media (max-width: 600px) { */
	@media (max-aspect-ratio: 3/4) {
		.sticky-image img.contain {
			padding-top: 12vw;
		}

		.fading-text-section {
    		width: 92vw;
			height: calc(100vh - 96vw - 30vw);
			margin-top: calc(100vw + 12vw);
		}

		:global(.fading-text-wrapper p) {
			font-size: min(5rem, 14px) !important;
			line-height: 28px;
			margin-top: 0;
		}
	}

	/* @media (max-width: 500px) { */
	@media (max-aspect-ratio: 2/3) {
		.image-container {
			z-index: 1;
		}

		.sticky-image img {
			object-fit: cover;
		}

		.sticky-image img.contain {
			padding-top: 15vw;
		}
		.fading-text-section {
    		width: 92vw;
			height: calc(100vh - 96vw - 30vw);
			margin-top: calc(100vw + 15vw);
		}

		:global(.fading-text-wrapper p) {
			font-size: min(8rem, 14px) !important;
			line-height: 28px;
			margin-top: 0;
		}
	}

	/* @media (max-width: 400px) { */
	@media (max-aspect-ratio: 1/2) {

		.sticky-image img.contain {
			padding-top: 40vw;
		}
		.fading-text-section {
    		width: 92vw;
			height: calc(100vh - 96vw - 4vw);
			margin-top: calc(100vw + 40vw);
		}


		:global(.fading-text-wrapper p) {
			font-size: min(5.5rem, 14px) !important;
			line-height: 24px;
		}
	}

</style>
