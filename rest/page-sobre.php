<?php
//Template Name: Sobre
?>

<?php get_header(); ?>
<?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
		<section class="container sobre">
			<h2 class="subtitulo"><?php the_title(); ?></h2>

			<div class="grid-8">
				<img src="<?php the_field('foto_rest'); ?>" alt="<?php the_field('foto_rest_descricao'); ?>">
			</div>

			<div class="grid-8">
				<h2><?php the_field('titulo_historia'); ?></h2>
				<p><?php the_field('texto_da_historia'); ?></p>
				
				<h2><?php the_field('titulo_visao'); ?></h2>
				<p><?php the_field('texto_visao'); ?></p>
				<h2><?php the_field('titulo_valores'); ?></h2>
				<p><?php the_field('texto_valores'); ?></p>
			</div>
		</section>
		<?php endwhile; else: endif; ?>
<?php get_footer(); ?>	