<script>
	import { onMount } from 'svelte';

	// props
	export let lineColour = '#000';
	export let dotFill = '#000';
	export let dotStroke = '#fff';
	export let dotRadius = 4;
	export let padding = 6; // horizontal padding inside SVG

	let width = 0;
	let height = 40;
	let svgEl;

	onMount(() => {
		const update = () => width = svgEl.clientWidth;
		update();
		const observer = new ResizeObserver(update);
		observer.observe(svgEl);
		return () => observer.disconnect();
	});

	// positions for 5 dots (spaced evenly between padding and width - padding)
	$: positions = Array.from({ length: 5 }, (_, i) =>
		padding + ((width - 2 * padding) / 4) * i
	);
</script>

<svg
	bind:this={svgEl}
	viewBox={`0 0 ${width} ${height}`}
	preserveAspectRatio="none"
	style="width:100%; height:auto; display:block;"
>
	<!-- horizontal line -->
	<line
		x1={positions[0]}
		y1={height / 2}
		x2={positions[positions.length - 1]}
		y2={height / 2}
		stroke={lineColour}
		stroke-width="2"
	/>

	<!-- dots -->
	{#each positions as x}
		<circle
			cx={x}
			cy={height / 2}
			r={dotRadius}
			fill={dotFill}
			stroke={dotStroke}
			stroke-width="2"
		/>
	{/each}
</svg>
