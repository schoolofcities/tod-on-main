<script>
	
	import "../assets/global-styles.css";

	// Image A
	export let imageURL1 = '';
	export let caption1 = '';
	export let source1 = '';
	export let altText1 = '';
	export let buttonLabel1 = 'Image 1';

	// Image B
	export let imageURL2 = '';
	export let caption2 = '';
	export let source2 = '';
	export let altText2 = '';
	export let buttonLabel2 = 'Image 2';

	// Shared
	export let maxWidth = '';
	export let link = 'Yes'; // Yes or No
	export let maxCaptionWidth = '680px';

	let active = 1;

</script>

<div
	class="img-container"
	style="max-width: {maxWidth};"
>

	<div class="toggle-buttons">
		<button
			class:active={active === 1}
			on:click={() => active = 1}
		>
			{buttonLabel1}
		</button>

		<button
			class:active={active === 2}
			on:click={() => active = 2}
		>
			{buttonLabel2}
		</button>
	</div>

	<div class="image-stack">
		{#if link === 'Yes'}
			<a href={imageURL1} target="_blank" class="image-layer" class:visible={active === 1}>
				<img src={imageURL1} alt={altText1} loading="lazy" />
			</a>

			<a href={imageURL2} target="_blank" class="image-layer" class:visible={active === 2}>
				<img src={imageURL2} alt={altText2} loading="lazy" />
			</a>
		{:else}
			<div class="image-layer" class:visible={active === 1}>
				<img src={imageURL1} alt={altText1} loading="lazy" />
			</div>

			<div class="image-layer" class:visible={active === 2}>
				<img src={imageURL2} alt={altText2} loading="lazy" />
			</div>
		{/if}
	</div>

	<div class="caption-container">
		<p>
			{#if active === 1}
				<span class="caption-text">{@html caption1}</span>
				<span class="caption-source">{@html source1}</span>
			{:else}
				<span class="caption-text">{@html caption2}</span>
				<span class="caption-source">{@html source2}</span>
			{/if}
		</p>
	</div>

</div>

<style>
	.img-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin: 0 auto;
		padding-top: 10px;
		padding-bottom: 0;
		margin-bottom: 30px;
		padding-left: 20px;
		padding-right: 20px;
	}

	.toggle-buttons {
		display: flex;
		gap: 10px;
		margin-bottom: 10px;
	}

	button {
		font-family: InterRegular;
		background: none;
		border: 1px solid #ccc;
		padding: 6px 12px;
		cursor: pointer;
		font-size: 14px;
	}

	button.active {
		border-color: #000;
		font-weight: 600;
	}

	.image-stack {
		position: relative;
		width: 100%;
	}

	.image-layer {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		opacity: 0;
		pointer-events: none;
		transition: opacity 0.4s ease;
	}

	.image-layer.visible {
		opacity: 1;
		pointer-events: auto;
		position: relative;
	}

	img {
		width: 100%;
		height: auto;
		max-height: 80dvh;
		min-height: 200px;
		display: block;
		object-fit: cover;
		object-position: center;
	}

	a {
		display: block;
		width: 100%;
	}

	a:hover {
		opacity: 0.95;
	}
</style>
