<script>
  import { fade } from "svelte/transition";
  import { onMount, onDestroy } from "svelte";

  export let imageAlign = "center";
  export let textSectionAlign = "right";
  export let textSectionMaxWidth = "500px";
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

<div class="scrolly-wrapper" bind:this={container}>
  <div class="sticky-image">
    {#each sections as section, i}
      {#if currentIndex === i}
        <div class="image-container">
          <img
            class={imageAlign}
            src={section.image}
            alt={section.heading}
            transition:fade={{ duration: 250 }}
            loading="lazy"
          />
        </div>
      {/if}
    {/each}
  </div>

  {#each sections as section, i}
    <div
      class="text-section {textSectionAlign}"
      bind:this={textSections[i]}
      style="max-width: {textSectionMaxWidth};"
    >
      <div class="text-wrapper {section.text.trim() ? '' : 'transparent'}">
        {@html section.text}
      </div>
    </div>
  {/each}
</div>

<style>
  .scrolly-wrapper {
    display: flex;
    flex-direction: column;
    position: relative;
  }

  .sticky-image {
    position: sticky;
    top: 10vh;
    height: 8z0dvh;
    height: 80vh;
    margin: 0 5vw;
    z-index: 0;
  }

  .sticky-image img {
    position: absolute;
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    border: 1px solid #ccc;
  }

  img.right {
    right: 0;
  }

  img.left {
    left: 0;
  }

  img.center {
    left: 50%;
    transform: translateX(-50%);
  }

  .text-wrapper {
    position: relative;
    z-index: 1;
    padding: 1em;
    margin: 0 5vw;
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid #ccc;
  }

  .text-wrapper.transparent {
    background: transparent !important;
    border: none !important;
    opacity: 0;
    pointer-events: none;
    box-shadow: none;
  }

  .text-section {
    padding: 30vh 2rem;
    /* width: 100%; */
    position: relative;
    z-index: 1;
    /* margin: 0 auto; */
    text-align: left;
    height: 90vh;
  }

  .text-section.center {
    margin: 0 auto;
  }
  .text-section.right {
    margin: 0 0 0 auto;
  }
  .text-section.left {
    margin: 0 0 0 0;
  }

  @media (max-width: 600px) {
    .text-section {
      padding: 30vh 1rem;
    }
  }
</style>
