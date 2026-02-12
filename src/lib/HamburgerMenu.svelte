<script>

	import "../assets/global-styles.css";  
	import { onMount } from "svelte";
    // import { tick } from 'svelte';

	export let iconColour = "black";
    export let contents = [];
    export let menuColour = "#e2e2e2"
    export let textColour = "black";

    let opened = false;
    let menu;

    let xColour = iconColour;

    $: xColour = opened ? "black" : iconColour;
    
    function handleKeydown(e) {
        if (e.key === 'Escape') {
            opened = false;
            document.querySelector('.hamburger-container')?.focus();
        }
    }

    function triggerMenu() {
        opened = !opened;

        // if (opened) {
        //     await tick();
        //     const firstLink = document.querySelector('#menu-content a');
        //     firstLink?.focus();
        // }
    }

    onMount(() => {
        menu = document.getElementById("menu");
    }) 

</script>


<div>
    <button
        class="hamburger-container"
        class:opened
        on:click={triggerMenu}
        aria-label="Navigation Menu"
        aria-expanded={opened}
        aria-controls="menu-content"
        on:keydown={handleKeydown}>
        <svg 
            class="icon"
            height="5.3rem"
            width="7rem"
            viewBox="0 0 215.2673 163.80329">

            <rect fill={xColour} class="bar top" x="0" y="0" width="215" height="23" rx="12" />

            <!-- middle bar -->
            <rect fill={xColour} class="bar middle" x="0" y="75" width="215" height="23" rx="12" />

            <!-- bottom bar -->
            <rect fill={xColour} class="bar bottom" x="0" y="150" width="215" height="23" rx="12" />
        
        </svg>
    </button>

    <div class="menu" 
        style:height="100vh"
        style:background-color={menuColour}
        class:opened
        >
        {#if opened}
            <nav id="menu-content">
                <a href="#top" style:color={textColour}>Title</a>

                {#each contents as content}
                    <a href={`#${content.item_id}`} 
                    style:color={textColour} 
                    on:click={() => {opened = false;}}>{content.menu_entry}</a>
                {/each}
            </nav>
        {/if}
    </div>

</div>



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

    .icon {
        overflow: visible;
    }

    .bar {
    transform-box: fill-box;
    transform-origin: center;
    transition:
        transform 300ms cubic-bezier(0.4, 0, 0.2, 1),
        opacity 200ms ease;
    }

    .hamburger-container.opened .bar.top {
    transform: translateY(75px) rotate(45deg) ;
    }

    .hamburger-container.opened .bar.middle {
    opacity: 0;
    }

    .hamburger-container.opened .bar.bottom {
    transform: translateY(-75px) rotate(-45deg) ;
    }

    .menu {
        width: 25vw;
        right: 0;
        transform: translateX(25vw);
        transition: transform 300ms cubic-bezier(0.4, 0, 0.2, 1);
        z-index: 25;
        position: fixed;
        display: flex;
        align-items: center;
    }

    .menu.opened {
        transform: translateX(0vw);
    }

    #menu-content {
        margin-left: 10%;
    }

    a {
        color: black;
        font-size: 6rem;
        font-family: PoppinsSemiBold;
        display: block;
        padding-bottom: 7rem;
        text-decoration: none;
    }

    a:hover {opacity: 60%;}

    @media (max-aspect-ratio: 5/6) {
        .menu {
            width: 100vw;
            transform: translateX(100vw);
        }
    }
    

</style>