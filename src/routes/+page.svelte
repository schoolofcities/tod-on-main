<script>
    import Top from "$lib/TopSofC.svelte";
    import Scrolly from "$lib/ScrollyImages.svelte";

    import amrothLot from "../assets/amroth-iso-lot.svg";
    import amrothBldg from "../assets/amroth-iso-bldg.svg";
    import wilsonLot from "../assets/wilson-iso-lot.svg";
    import wilsonBldg from "../assets/wilson-iso-bldg.svg";

    import "../assets/styles.css";

    const imageAlign = "center"; // options: "left", "center", "right"
    const textSectionAlign = "center"; // options: "left", "center", "right"
    const textSectionMaxWidth = "600px"; // max width of text sections, they will shrink to fit smaller screens
    const scrollyContent = [
        {
            image: amrothLot,
            text: "<h2>Header</h2> <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
        },
        {
            image: amrothBldg,
            text: "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"
        },
        {
            image: wilsonLot,
            text:"", // empty text section to demonstrate transparent div
        },
        {
            image: wilsonBldg,
            text: "<h2>Header</h2> <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>",
        },
    ];
</script>

<svelte:head>
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1, minimum-scale=1"
    />
    <script
        src="https://unpkg.com/maplibre-gl@4.3.2/dist/maplibre-gl.js"
    ></script>
</svelte:head>

<Top />

<main>
    <div class="title">
        <h1>Scrolly Images Example</h1>
        <h3>This is an example of scrolly telly with images.</h3>
        <p class="author">
            <a href="" target="_blank">Author 1</a>,
            <a href="" target="_blank">Author 2</a>,
            <a href="" target="_blank">Author 3</a> | Month 2025
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>
    <div class="article">
        <h2>Header 1</h2>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>

    <Scrolly sections={scrollyContent} imageAlign={imageAlign} textSectionMaxWidth={textSectionMaxWidth} textSectionAlign={textSectionAlign} />

    <div class="article">
        <h2>Header 2</h2>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>
</main>
