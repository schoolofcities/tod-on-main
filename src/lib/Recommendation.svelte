<script>
	// import '../assets/global-styles.css';

	export let style = 3;
	export let title = "Title";
	export let count;

</script>

<div class={`style-${style} container`}>
	<div class="box"><h3 class="recommendation">RECOMMENDATION {count}:</h3></div>
	<h3 class="title">{title}</h3>
</div>

<style>

	.container {
		margin-top: 50px;
		display: flex;
		position: relative;
	}

	.box {
		max-width: 300px;
  		margin-left: calc(-50% + 45px);
		padding: 15px 30px 15px 30px;
	}

	.recommendation {
		white-space: nowrap;
		overflow: hidden;
	}

	h3 {
		margin: 0;
	}

	.title {
		padding: 8px 0 15px 15px;
	}

	
	.style-1.container {
		align-items: start;
	}

	.box h3 {
		font-size: 22px;
	}

	.style-1 .box {
		background-color: rgb(0, 0, 0, 0.1);
	}

	.style-2 .box, .style-3 .box {
		width: fit-content;
		background-color: rgb(0, 0, 0, 0.1);
	}

	.style-1 .title, .style-2 .title,.style-3 .title {
		border-top: 5px solid rgb(0, 0, 0, 0.1);
	}

	.style-2.container,.style-3.container {
		align-items: stretch;
	}

	.style-3 .box {
		/* border-radius: 25px; */
		display: flex;
		align-items: center; 
	}

	.style-4.container {
		align-items: center;
	}

	.style-4 .box {
  		margin-left: calc(-50% + 5px);
		border-radius: 25px;
		background-color: rgb(0, 0, 0, 0.1);
	}


	@media (max-width: 1300px) {
		.container {
			display: inline;
			position: relative;
		}

		.box {
			margin-top: 50px;
			width: fit-content;
			margin-left: 0;
		}

		.box h3 {
			font-size: 20px;
		}
		
		.style-1 .title, .style-2 .title,.style-3 .title {
			border-left: 5px solid rgb(0, 0, 0, 0.1);
			border-top: none;
		}

	}


</style>
