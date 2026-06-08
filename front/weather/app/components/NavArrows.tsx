"use client";

import { useRouter } from "next/navigation";

export default function NavigationArrows({
  currentId,
  allIds,
}: {
  currentId: number;
  allIds: number[];
}) {
  const router = useRouter();

  const index = allIds.indexOf(currentId);
  const prevId = index > 0 ? allIds[index - 1] : null;
  const nextId = index < allIds.length - 1 ? allIds[index + 1] : null;

  return (
    <>
      {/* LEFT */}
      {prevId !== null && (
        <div
          onClick={() => router.push(`/${prevId}`)}
          className="fixed left-0 top-0 h-full w-16 flex items-center justify-center cursor-pointer group"
        >
          <div className="pixel-border bg-atari-black text-atari-yellow p-3 opacity-60 group-hover:opacity-100 font-pixel">
            {"<"}
          </div>
        </div>
      )}

      {/* RIGHT */}
      {nextId !== null && (
        <div
          onClick={() => router.push(`/${nextId}`)}
          className="fixed right-0 top-0 h-full w-16 flex items-center justify-center cursor-pointer group"
        >
          <div className="pixel-border bg-atari-black text-atari-yellow p-3 opacity-60 group-hover:opacity-100 font-pixel">
            {">"}
          </div>
        </div>
      )}
    </>
  );
}
