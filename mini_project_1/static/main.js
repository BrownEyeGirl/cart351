import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';


const MODEL_PATH = '/static/cookie.glb';

const canvas = document.getElementById('scene');
const info = document.getElementById('info');

// Basic scene setup
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(window.devicePixelRatio);

const scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff);
const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 1.5, 4);

const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;

scene.add(new THREE.HemisphereLight(0xffffff, 0x444444, 2));
const sun = new THREE.DirectionalLight(0xffffff, 2);
sun.position.set(5, 10, 7);
scene.add(sun);

let mixer = null;
let modelToFrame = null;
const clock = new THREE.Clock();

function resizeRenderer() {
  const width = canvas.clientWidth;
  const height = canvas.clientHeight;
  if (!width || !height) return;

  renderer.setSize(width, height, false);
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  if (modelToFrame) frameModel(modelToFrame);
}

const canvasResizeObserver = new ResizeObserver(resizeRenderer);
canvasResizeObserver.observe(canvas);


new GLTFLoader().load(
  MODEL_PATH,
  (gltf) => {
    const animations = gltf.animations;

    console.log('Number of animations:', animations.length);
    animations.forEach((clip, i) => console.log(`  ${i}: ${clip.name || '(unnamed)'}`));

    if (info) {
      info.innerHTML = `Animations: ${animations.length}`
        + animations.map((clip, i) => `<br>${i}: ${clip.name || '(unnamed)'}`).join('');
    }

    scene.add(gltf.scene);
    modelToFrame = gltf.scene;
    resizeRenderer();


    mixer = new THREE.AnimationMixer(gltf.scene); //doesnt play animations until clicked 

    // Stops the other animation and plays this one from the start
    function playOnly(action) {
      if (!action) return;
      mixer.stopAllAction();
      action.setLoop(THREE.LoopOnce); // play one time only
      action.clampWhenFinished = true; // hold the last frame instead of snapping back
      action.reset().play();
    }

    // Connect the existing page buttons to the matching clips in cookie.glb.
    const animationForButton = {
      'file': 'file',
      'cake': 'birthday cakeAction',
      'cookie': 'cookie',
      'adhd pill': 'pill',
      'airplane': 'airplane'
    };

    const actions = new Map(animations.map((clip) => [
      clip.name.trim().toLowerCase(),
      mixer.clipAction(clip)
    ]));

    document.querySelectorAll('.button-grid button').forEach((button) => {
      const buttonName = button.textContent.trim().toLowerCase();
      const clipName = animationForButton[buttonName];
      const action = clipName && actions.get(clipName.toLowerCase());

      if (action) {
        button.addEventListener('click', () => playOnly(action));
      }
    });
  },
  undefined,
  (error) => {
    console.error('Error loading GLB:', error);
    if (info) info.textContent = `Couldn't load ${MODEL_PATH}. Check the console.`;
  }
);

// Points the camera at the model, whatever its size; might want to fuck around with this 
function frameModel(object) {
  const box = new THREE.Box3().setFromObject(object);
  const center = box.getCenter(new THREE.Vector3());
  const sphere = box.getBoundingSphere(new THREE.Sphere());
  const verticalFov = THREE.MathUtils.degToRad(camera.fov);
  const horizontalFov = 2 * Math.atan(Math.tan(verticalFov / 2) * camera.aspect);
  const distance = Math.max(
    sphere.radius / Math.sin(verticalFov / 2),
    sphere.radius / Math.sin(horizontalFov / 2)
  ) * 1.08;

  controls.target.copy(center);
  camera.position.copy(center).add(new THREE.Vector3(0, 0.15, 1).normalize().multiplyScalar(distance));
  camera.near = Math.max(distance / 100, 0.01);
  camera.far = distance * 100;
  camera.updateProjectionMatrix();
}

window.addEventListener('resize', resizeRenderer);

renderer.setAnimationLoop(() => {
  if (mixer) mixer.update(clock.getDelta());
  controls.update();
  renderer.render(scene, camera);
});
