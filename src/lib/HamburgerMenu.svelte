<script>

	import "../assets/global-styles.css";  

	export let colour = "black";


</script>

<button class="hamburger-container"
    on:click={null}
    aria-label="Expand Navigation Menu">
    <svg
    width="7rem"
    height="5.3rem"
    viewBox="0 0 215.2673 163.80329"
    version="1.1"
    id="svg1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:svg="http://www.w3.org/2000/svg">
    <defs
        id="defs1" />
    <g
        id="layer1"
        transform="translate(-10.166061,-107.8184)">
        <path
        style="fill:{colour};stroke-width:0.264583"
        d="M 43.427509,117.03346 112.6171,182.17472"
        id="path1" />
        <path
        style="fill:{colour};stroke-width:0.264583"
        d="M 132.12268,186.95911 46.371748,120.34572"
        id="path2" />
        <rect
        style="fill:{colour};stroke-width:0.325973"
        id="rect3"
        width="23.185873"
        height="215.07222"
        x="107.8184"
        y="-225.23828"
        ry="17.596819"
        transform="rotate(90)"
        rx="11.592937" />
        <rect
        style="fill:{colour};stroke-width:0.325973"
        id="rect3-2"
        width="23.185873"
        height="215.07222"
        x="178.35234"
        y="-225.26613"
        ry="17.596819"
        transform="rotate(90)"
        rx="11.592937" />
        <rect
        style="fill:{colour};stroke-width:0.325973"
        id="rect3-2-2"
        width="23.185873"
        height="215.07222"
        x="248.43582"
        y="-225.43336"
        ry="17.596819"
        transform="rotate(90)"
        rx="11.592937" />
    </g>
    </svg>
</button>

<style>
    .hamburger-container {
        width: fit-content;
        height: fit-content;
        cursor:pointer;
        border: none;
        background-color: rgb(0,0,0,0);
        position: fixed;
		z-index: 100;
        top: 15rem;
        right: 15rem;
    }

</style>