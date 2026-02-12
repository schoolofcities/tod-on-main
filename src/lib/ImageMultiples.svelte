<script>
	export let images = []; // Array of objects containing image urls, caption text in markdown, alt text
	export let mainCaption = null;
	export let matchWidth = true;
	export let matchHeight = true;
	export let imageFit = "cover"; // object-fit properties for images

    import { marked } from 'marked';

	let layoutClass = '';
	// let imgs = []; // This will hold the loaded image elements
	let container;

	const updateLayout = () => {
		const width = window.innerWidth;

		if (images.length === 2) {
			layoutClass = width < 740 ? 'stack-2' : 'row-2';
		} else if (images.length === 3) {
			if (width < 360 * 3) {
				layoutClass = width < 740 ? 'stack-3' : 'two-plus-one';
			} else {
				layoutClass = 'row-3';
			}
		} else if (images.length === 4) {
			layoutClass = width < 740 ? 'stack-4' : 'grid-2x2';
		}
	};

	import { onMount, onDestroy } from 'svelte';

	onMount(() => {
		const observer = new IntersectionObserver(async ([entry]) => {
			if (entry.isIntersecting) {
				// await loadAllImages();
				updateLayout();
				
				observer.disconnect();
			}
		}, {
			rootMargin: '200px' // Start loading when within 200px of viewport
		});
				
		// Setup resize listener after loading
		window.addEventListener('resize', updateLayout);

		if (container) observer.observe(container);

		onDestroy(() => {
			window.removeEventListener('resize', updateLayout);
		});
	});
</script>

<div class="img-grid {layoutClass}" bind:this={container}>
	{#each images as image}
		<div>
			<div class="img-box {matchWidth ? "match-width" : ""} {matchHeight ? "match-height" : ""}">
				<img src={image.url} alt={image.alt} style:object-fit={imageFit}/>
			</div>
			<p>{image.caption}</p>
		</div>
	{/each}
	
	{#if mainCaption}
		<p>{@html marked(mainCaption)}</p>
	{/if}
</div>

<style>
	.img-grid {
		display: flex;
		/* flex-wrap: wrap; */
		justify-content: center;
		gap: 10px;
		height: fit-content;
	}

	.img-box {
		width: auto;
		height: auto;
	}

	.img-box.match-width {
		width: 360px;
	}

	.img-box.match-height {
		height: 40dvh;
	}

	.match-width img {
		width: 100%;
	}

	.match-height img {
		height: 40dvh;
	}

	img {
		max-width: 40dvw;
		max-height: 40dvh;
	}

	@media (max-width: 700px) {
		img {
			max-width: 90dvw;
			max-height: 40dvh;
		}
	}


	/* Layout classes */
	.row-2, .row-3 {
		flex-direction: row;
	}

	.stack-2, .stack-3, .stack-4 {
		flex-direction: column;
		align-items: center;
	}

	.two-plus-one {
		display: grid;
		grid-template-columns: repeat(2, 360px);
		grid-template-rows: auto auto;
		justify-content: center;
	}

	.two-plus-one .svg-box:nth-child(3) {
		grid-column: 1 / span 2;
		justify-self: center;
	}

	.grid-2x2 {
		display: grid;
		grid-template-columns: repeat(2, 360px);
		grid-template-rows: repeat(2, auto);
		justify-content: center;
	}
</style>
