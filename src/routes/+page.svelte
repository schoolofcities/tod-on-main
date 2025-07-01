<script>
    import ImageScroller from "$lib/ImageScroller.svelte";
    import ImageFader from "$lib/ImageFader.svelte";

    import amrothLot from "../assets/amroth-iso-lot.svg";
    import amrothBldg from "../assets/amroth-iso-bldg.svg";
    import wilsonLot from "../assets/wilson-iso-lot.svg";
    import wilsonBldg from "../assets/wilson-iso-bldg.svg";

    const imageUrls = [amrothLot, amrothBldg];
</script>

<div class="spacer">Clip Path</div>

<ImageScroller images={imageUrls} />

<div class="spacer">Fade</div>

<ImageFader images={imageUrls} />

<div class="spacer"></div>

<style>
    .spacer {
        height: 100vh;
        overflow: hidden;
        border-top: 0.5px solid grey;
        border-bottom: 0.5px solid grey;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
    }
</style>
