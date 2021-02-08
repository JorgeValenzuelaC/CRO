let container;
let camera;
let renderer;
let scene;
let icecream;

import {OrbitControls} from "./OrbitControl.js"
import { DirectionalLight } from "./three.module.js";

function init(){
    container = document.querySelector('.scene');
    
    scene = new THREE.Scene();

    const fov = 50;
    const aspect = container.clientWidth / container.clientHeight;
    const near = 0.1;
    const far = 500;
    
    camera = new THREE.PerspectiveCamera(fov,aspect,near,far);
    camera.position.set(0,0,5);

    const ambient = new THREE.AmbientLight(0x404040,15);
    const directionalLight = new THREE.DirectionalLight( 0x404040,15);
    scene.add(ambient);

    renderer = new THREE.WebGLRenderer({antialias: true, alpha: true});
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);

    container.appendChild(renderer.domElement);

    var controls = new OrbitControls(camera, renderer.domElement);

    controls.minDistance = 3;
    controls.maxDistance = 20;
    controls.enableDamping = true

    let loader = new THREE.GLTFLoader(); 
    loader.load('../static/proyecto_web_app/img/F/scene.gltf', function(gltf){
      scene.add(gltf.scene);
      icecream = gltf.scene.children[0];
      animate();
    });
}
function animate(){
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

init()