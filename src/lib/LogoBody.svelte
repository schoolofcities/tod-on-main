<script>

	import "../assets/global-styles.css";
	import logoBlueColour from '../assets/sofc-uoft-logo-blue-colour.svg';
	import logoWhiteColour from '../assets/sofc-uoft-logo-white-colour.svg';
	import logoBlack from '../assets/sofc-uoft-logo-black.svg';
	import logoWhite from '../assets/sofc-uoft-logo-white.svg';

	const logo = logoBlueColour;

</script>

<a href="https://schoolofcities.utoronto.ca/" target="_blank">
	<img
		class="svg-logo"
		src={logo}
		alt="School of City logo"
		loading="lazy"
		draggable="false"
		tabindex="0"
	/>
</a>

<style>

.svg-logo {
    width: min(270px, 50%);
    max-width: 100%;
	margin-left: -7px;
    height: auto;
    display: block;
}

.svg-logo:hover {
	opacity: 0.7;
}

</style>