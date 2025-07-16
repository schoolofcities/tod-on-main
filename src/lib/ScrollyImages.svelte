<script>
  import { fade } from 'svelte/transition';
  import { onMount, onDestroy } from 'svelte';

  export let sections = [
    {
      image: "/images/1.jpg",
      heading: "Welcome to the Story",
      body: "This is the introduction. Scroll to learn more about each stage."
    },
    {
      image: "/images/2.jpg",
      heading: "The Conflict",
      body: "Here's where the tension begins. Characters face challenges."
    },
    {
      image: "/images/3.jpg",
      heading: "The Resolution",
      body: "The story concludes and everything comes together."
    }
  ];

  let container;
  let currentIndex = 0;
  let textSections = [];

  const handleScroll = () => {
    let newIndex = currentIndex;
    textSections.forEach((section, index) => {
      const rect = section.getBoundingClientRect();
      if (
        rect.top <= window.innerHeight * 0.5 &&
        rect.bottom > window.innerHeight * 0.5
      ) {
        newIndex = index;
      }
    });

    currentIndex = newIndex;
  };

  onMount(() => {
    window.addEventListener("scroll", handleScroll);
    handleScroll();
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  });
</script>

<style>
  .scrolly-wrapper {
    display: flex;
    flex-direction: column;
    position: relative;
  }

  .sticky-image {
    position: sticky;
    top: 0;
    height: 100dvh;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    z-index: 0;
  }

  .sticky-image img {
    position: absolute;
    top: 50%;
    left: 50%;
    max-width: 100%;
    max-height: 100%;
    transform: translate(-50%, -50%);
    object-fit: contain;
    border: 1px solid #ccc;
  }

  .text-wrapper {
    position: relative;
    z-index: 1;
    padding: 1em;
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid #ccc;
  }

  .text-section {
    padding: 30vh 2rem;
    position: relative;
    z-index: 1;
    margin: 0 auto;
    text-align: left;
    height: 95vh;
  }

  @media (max-width: 600px) {
  .text-section {
    padding: 30vh 1rem;
  }
  }

</style>

<div class="scrolly-wrapper" bind:this={container}>

<div class="sticky-image">
    {#each sections as section, i}
        {#if currentIndex === i}
            <div class="image-container">
                <img
                    src={section.image}
                    alt={section.heading}
                    transition:fade={{ duration: 250 }}
                />
            </div>
        {/if}
    {/each}
</div>

  {#each sections as section, i}
    <div class="text-section" bind:this={textSections[i]}>
      <div class="text-wrapper">
      <h2>{section.heading}</h2>
      <p>{@html section.body}</p>
      </div>
    </div>
  {/each}
</div>
