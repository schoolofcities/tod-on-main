<script>
  import { onMount } from "svelte";
  export let images = [];

  let sceneWrapper;
  let stickyContainer;

  onMount(async () => {
    const gsap = (await import("gsap")).default;
    const ScrollTrigger = (await import("gsap/ScrollTrigger")).default;
    gsap.registerPlugin(ScrollTrigger);

    const sections = sceneWrapper.querySelectorAll("section");

    sections.forEach((section, i) => {
      if (i === sections.length - 1) return;

      gsap.to(section, {
        clipPath: "polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%)",
        ease: "none",
        scrollTrigger: {
          trigger: sceneWrapper,
          start: () => `top+=${i * window.innerHeight} top`,
          end: () => `top+=${(i + 1) * window.innerHeight} top`,
          scrub: true,
        },
      });
    });
  });
</script>

<div
  bind:this={stickyContainer}
  class="scroll-container"
  style={`height: ${images.length * 100}vh;`}
>
  <div class="scene-wrapper" bind:this={sceneWrapper}>
    {#each images as image, i}
      <section class="panel" style="z-index: {images.length - i}">
        <div class="content">
          <img src={image} alt="" />
        </div>
      </section>
    {/each}
  </div>
</div>

<style>
  :global(html),
  :global(body) {
    margin: 0;
    padding: 0;
    height: 100%;
    overflow-x: hidden;
  }

  .scroll-container {
    position: relative;
    width: 100%;
  }

  .scene-wrapper {
    position: sticky;
    top: 0;
    height: 100vh;
  }

  .panel {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
  }

  .content {
    width: 100%;
    height: 100%;
  }

  .content img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }
</style>
