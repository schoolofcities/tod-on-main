<script>
	import "../assets/global-styles.css"
	export let images = []; // Array of objects containing image urls, caption text in markdown, alt text
	export let mainCaption = null;
	export let mainSource = null;
	export let maxWidth = 1080;
	export let imageFit = "cover"; // object-fit properties for images

	let gridWidth;

    import { marked } from 'marked';

	let layoutClass = '';
	// let imgs = []; // This will hold the loaded image elements
	let container;


</script>

<div class="img-container" style:max-width={maxWidth}> 
	<div class="img-grid" bind:this={container} bind:clientWidth={gridWidth}>
		{#each images as image}
			<div class="img-item">
				<div class="img-box">
					<img src={image.url} alt={image.alt} style:object-fit={imageFit} 
					style:max-width="{maxWidth/2}px"/>
				</div>
				{#if image.caption}
					<p>
						<span class="caption-text">{image.caption}</span>
					</p>
				{/if}
			</div>
		{/each}

	</div>
	
	{#if mainCaption || mainSource}
		<div class="caption-container" style:width="{gridWidth - 40}px">
			<p class="caption">
				{#if mainCaption}
					<span class="caption-text">{@html mainCaption}</span>
				{/if}
				{#if mainSource}
					<span class="caption-source">{@html mainSource}</span>
				{/if}
			</p>
		</div>
	{/if}
</div>

<style>
	.img-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-bottom: 30px;
		width: 100%;
	}

	.img-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
		padding-left: 20px;
		padding-right: 20px;
    }

	.img-item {
        min-width: 0; 
		max-width: 50dvw;
    }

    .img-box {
        width: 100%;
    }

	img {
        width: 100%;
        height: 100%;
        display: block;
    }

	.caption-container {
		width: 100%; 
		box-sizing: border-box;
	}

	@media (max-width: 700px) {
		
        .img-grid {
            grid-template-columns: 1fr;
			border: 0;
        }

		.img-item {
			max-width: 90dvw;
		}
	}

</style>
