<script>

	import "../assets/global-styles.css";  

	export let colour = "black";
    export let clickable = false;
    export let hidden = false;

	let scrollPage = () => {
		window.scrollBy({
			top: window.innerHeight,
			left: 0,
			behavior: "smooth",
		});
	}

</script>

<button class="arrow-container"
    on:click={clickable ? scrollPage : null}
    aria-label="Next Slide"
    class:hidden={hidden}>
    <svg
        width="7rem"
        height="4rem"
        viewBox="0 0 190.8009 107.01583"
        version="1.1"
        id="svg1"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:svg="http://www.w3.org/2000/svg">
        <defs
            id="defs1" />
        <g
            id="layer1"
            transform="translate(-9.9835959,-107.49872)">
            <path
                style="fill:{colour};stroke-width:0.264583"
                d="M 43.427509,117.03346 112.6171,182.17472"
                id="path1" />
            <path
                style="fill:{colour};stroke-width:0.264583"
                d="M 132.12268,186.95911 46.371748,120.34572"
                id="path2" />
            <rect
                style="fill:{colour};stroke-width:0.264583"
                id="rect3"
                width="23.185873"
                height="141.69145"
                x="-80.555573"
                y="87.898438"
                ry="11.592937"
                transform="rotate(-45)" />
            <rect
                style="fill:{colour};stroke-width:0.264583"
                id="rect3-8"
                width="23.185873"
                height="141.69145"
                x="206.39622"
                y="-61.146145"
                ry="11.592937"
                transform="rotate(45)" />
        </g>
    </svg>
</button>


<style>
    .arrow-container {
        width: fit-content;
        height: fit-content;
        cursor:pointer;
        border: none;
        background-color: rgb(0,0,0,0);
        position: fixed;
		z-index: 100;
		bottom: 10rem;
        left: 50%;
        margin-left: -3.5rem;
        display: inline-block;
    }

    .hidden {
        display: none;
    }

</style>