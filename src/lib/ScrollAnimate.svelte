<script>

	import "../assets/global-styles.css";  
	import { onMount } from "svelte";

	export let colour = "black";   
    let shown = false;
	
	let scrollTimeout;

	function onPageStill() {
	 	shown = true;
	}

    const handleScroll = () => {
		clearTimeout(scrollTimeout);
		shown = false;
		scrollTimeout = setTimeout(onPageStill, 5000);
	};

    onMount(() => {
		window.addEventListener("scroll", handleScroll);
		handleScroll();
		return () => {
			window.removeEventListener("scroll", handleScroll)
		};
	});

</script>

<div class="arrow-container" style:display={shown ? "flex" : "none"}>
    <svg
        width="7rem"
        height="4rem"
        viewBox="0 0 190.8009 107.01583"
        version="1.1"
        class="arrow"
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
    <svg
        width="7rem"
        height="4rem"
        viewBox="0 0 190.8009 107.01583"
        version="1.1"
        class="arrow"
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
</div>

<style>
    .arrow-container {
        width: 8rem;
        height: fit-content;
        border: none;
        background-color: rgb(0,0,0,0);
        position: fixed;
		z-index: 50;
        right: 15rem;
        bottom: 15rem;
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .arrow {
        animation: fadeBounce 1.5s ease-in-out infinite;
    }

    @keyframes fadeBounce {
    0% {
        opacity: .7;
        transform: translateY(0);
    }
    50% {
        opacity: .5;
        transform: translateY(10px);
    }
    100% {
        opacity: .7;
        transform: translateY(0);
    }
    }

</style>